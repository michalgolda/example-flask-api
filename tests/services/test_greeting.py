from services.greeting import GreetingService

def test_greeting_service():
    service = GreetingService()
    service_output = service.execute("John")

    assert service_output == "Hello, John!" 