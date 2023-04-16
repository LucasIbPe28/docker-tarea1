import grpc
import spacex_pb2
import spacex_pb2_grpc

def create_client():
    channel = grpc.insecure_channel('api.spacexdata.com:443')
    return spacex_pb2_grpc.SpaceXStub(channel)


def search_rocket(client):
    rocket_id = "falcon9"
    request = spacex_pb2.RocketRequest(rocket_id=rocket_id)
    rocket = client.GetRocket(request)
    return rocket

if __name__ == "__main__":
    client = create_client()
    rocket = search_rocket(client)
    print("Rocket ID:", rocket.rocket_id)
    print("Rocket Name:", rocket.rocket_name)
    print("Rocket Type:", rocket.rocket_type)

