import grpc
import ssl
import spacex_pb2
import spacex_pb2_grpc


context = ssl.create_default_context()
context.load_verify_locations('spacex.crt')


channel = grpc.secure_channel('api.spacexdata.com:443', grpc.ssl_channel_credentials(context))


client = spacex_pb2_grpc.LaunchServiceStub(channel)


request = spacex_pb2.GetLaunchRequest(flight_number=1)
response = client.GetLaunch(request)

print(response)

