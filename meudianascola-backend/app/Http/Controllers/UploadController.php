<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\StorageService;
use App\Services\FirebaseService;
use Illuminate\Support\Str;

class UploadController extends Controller
{
    protected $storageService;
    protected $firebase;

    public function __construct(StorageService $storageService, FirebaseService $firebase)
    {
        $this->storageService = $storageService;
        $this->firebase = $firebase;
    }

    public function uploadPhoto(Request $request)
    {
        $validated = $request->validate([
            'studentId' => 'required|string',
            'file' => 'required|file|mimes:jpg,jpeg,png'
        ]);

        $file = $request->file('file');
        $tmpPath = $file->getPathname();
        $ext = $file->getClientOriginalExtension();
        $remotePath = 'daily/' . $validated['studentId'] . '/' . Str::random(12) . '.' . $ext;

        $result = $this->storageService->uploadFromPath($tmpPath, $remotePath);

        $doc = [
            'studentId' => $validated['studentId'],
            'date' => now()->toDateString(),
            'createdAt' => now()->toDateTimeString(),
            'photos' => [$result['path']],
            'notes' => 'Foto enviada pelo professor'
        ];
        $this->firebase->addDocument('dailyRecords', $doc);

        return response()->json(['message' => 'Upload realizado', 'url' => $result['url']], 201);
    }
}
