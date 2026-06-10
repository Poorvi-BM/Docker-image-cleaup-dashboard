import docker

client = docker.from_env()

def get_all_images():
    images = client.images.list()

    result = []

    for image in images:
        result.append({
            "id": image.short_id,
            "tags": image.tags,
            "size": round(image.attrs["Size"] / (1024**2), 2)
        })

    return result