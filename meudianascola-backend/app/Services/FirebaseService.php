<?php
namespace App\Services;

use Kreait\Firebase\Factory;

class FirebaseService
{
    protected $firestore;

    public function __construct()
    {
        $factory = (new Factory)
            ->withServiceAccount(base_path(env('FIREBASE_CREDENTIALS')))
            ->withDatabaseUri(env('FIREBASE_DB_URL'));
        $this->firestore = $factory->createFirestore()->database();
    }

    public function addDocument($collection, $data)
    {
        return $this->firestore->collection($collection)->add($data);
    }

    public function getDocuments($collection)
    {
        return $this->firestore->collection($collection)->documents();
    }

    public function getDocument($collection, $docId)
    {
        return $this->firestore->collection($collection)->document($docId)->snapshot();
    }
}
