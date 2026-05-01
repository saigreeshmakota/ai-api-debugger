import time

def measure_latency(func, *args, **kwargs):
    start = time.time()
    response = func(*args, **kwargs)
    end = time.time()

    latency = round(end - start, 2)
    return response, latency


def parse_error(response):
    try:
        return response.json().get("error", {}).get("message", "Unknown error")
    except:
        return "Error parsing response"