from google.cloud.storage import Client

client = Client()


def main() -> None:
    bucket_name = "bkt-landing-zone-de-with-python"
    bucket = client.bucket(bucket_name=bucket_name)
    blob = bucket.blob("hello.txt")

    blob.upload_from_filename("hello.txt")


if __name__ == "__main__":
    main()
