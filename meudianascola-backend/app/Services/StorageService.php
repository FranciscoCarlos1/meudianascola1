<?php
namespace App\Services;

use Kreait\Firebase\Factory;

class StorageService
{
    protected $bucket;

    public function __construct()
    {
        $factory = (new Factory)
            ->withServiceAccount(base_path(env('FIREBASE_CREDENTIALS')));
        $bucketName = env('FIREBASE_STORAGE_BUCKET');
        $this->bucket = $factory->createStorage()->getBucket($bucketName);
    }

    public function uploadFromPath($localPath, $remotePath)
    {
        $object = $this->bucket->upload(fopen($localPath, 'r'), [
            'name' => $remotePath
        ]);
        $expiresAt = new \DateTime('+1 hour');
        $url = $object->signedUrl($expiresAt);
        return ['path' => $remotePath, 'url' => $url];
    }
}
