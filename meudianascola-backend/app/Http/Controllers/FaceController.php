<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Services\FaceApiService;
use App\Services\FirebaseService;

class FaceController extends Controller
{
    protected $faceService;
    protected $firebase;

    public function __construct(FaceApiService $faceService, FirebaseService $firebase)
    {
        $this->faceService = $faceService;
        $this->firebase = $firebase;
    }

    public function register(Request $request)
    {
        $validated = $request->validate([
            'userId' => 'required|string',
            'imageUrl' => 'required|url'
        ]);

        $detect = $this->faceService->detect($validated['imageUrl']);
        return response()->json(['detect' => $detect]);
    }

    public function verify(Request $request)
    {
        $validated = $request->validate([
            'faceIds' => 'required|array'
        ]);

        $identify = $this->faceService->identify($validated['faceIds']);
        return response()->json(['identify' => $identify]);
    }
}
