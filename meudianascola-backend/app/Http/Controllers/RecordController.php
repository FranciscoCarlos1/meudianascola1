<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\FirebaseService;

class RecordController extends Controller
{
    protected $firebase;

    public function __construct(FirebaseService $firebase)
    {
        $this->firebase = $firebase;
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'studentId' => 'required|string',
            'date' => 'required|string',
            'meals' => 'nullable|array',
            'naps' => 'nullable|array',
            'diaperChanges' => 'nullable|integer',
            'mood' => 'nullable|string',
            'notes' => 'nullable|string',
            'photos' => 'nullable|array'
        ]);

        $validated['createdAt'] = now()->toDateTimeString();

        $this->firebase->addDocument('dailyRecords', $validated);

        return response()->json(['message' => 'Registro diário salvo com sucesso!'], 201);
    }

    public function index($studentId)
    {
        $records = $this->firebase->getDocuments('dailyRecords');
        $filtered = [];

        foreach ($records as $record) {
            $data = $record->data();
            if (isset($data['studentId']) && $data['studentId'] === $studentId) {
                $filtered[] = array_merge(['id' => $record->id()], $data);
            }
        }

        return response()->json($filtered, 200);
    }
}
