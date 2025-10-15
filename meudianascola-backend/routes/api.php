<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\StudentController;
use App\Http\Controllers\RecordController;
use App\Http\Controllers\FaceController;
use App\Http\Controllers\UploadController;

// Health
Route::get('/health', function() { return response()->json(['status' => 'API OK - MeuDiaNaEscola']); });

Route::middleware('auth:sanctum')->group(function () {
    Route::get('/students', [StudentController::class, 'index']);
    Route::post('/students', [StudentController::class, 'store']);
    Route::get('/students/{id}', [StudentController::class, 'show']);

    Route::post('/records', [RecordController::class, 'store']);
    Route::get('/records/{studentId}', [RecordController::class, 'index']);

    Route::post('/upload/photo', [UploadController::class, 'uploadPhoto']);
    Route::post('/face/register', [FaceController::class, 'register']);
    Route::post('/face/verify', [FaceController::class, 'verify']);
});
