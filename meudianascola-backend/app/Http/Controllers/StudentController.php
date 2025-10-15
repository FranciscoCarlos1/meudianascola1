<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\FirebaseService;

class StudentController extends Controller
{
    protected $firebase;

    public function __construct(FirebaseService $firebase)
    {
        $this->firebase = $firebase;
    }

    public function index()
    {
        $students = $this->firebase->getDocuments('students');
        $data = [];

        foreach ($students as $student) {
            $data[] = array_merge(['id' => $student->id()], $student->data());
        }

        return response()->json($data, 200);
    }

    public function store(Request $request)
    {
        $validated = $request->validate([
            'name' => 'required|string',
            'dob' => 'required|string',
            'classId' => 'required|string',
            'guardians' => 'required|array',
        ]);

        $validated['createdAt'] = now()->toDateTimeString();

        $this->firebase->addDocument('students', $validated);

        return response()->json(['message' => 'Aluno cadastrado com sucesso!'], 201);
    }

    public function show($id)
    {
        $students = $this->firebase->getDocuments('students');
        foreach ($students as $student) {
            if ($student->id() === $id) {
                return response()->json($student->data(), 200);
            }
        }

        return response()->json(['message' => 'Aluno não encontrado'], 404);
    }
}
