import requests
import time
from kubernetes import client, config

def get_number_of_pods(deployment_name="httpd-deployment", namespace="fuji"):
    # Load Kubernetes configuration from default location
    config.load_kube_config()

    # Create a Kubernetes API client
    api_instance = client.AppsV1Api()

    try:
        # Get the deployment object
        deployment = api_instance.read_namespaced_deployment(deployment_name, namespace)

        # Get the number of replicas (desired and available)
        desired_replicas = deployment.spec.replicas
        available_replicas = deployment.status.available_replicas

        # Return the number of available replicas
        return available_replicas

    except Exception as e:
        print(f"Error: {e}")
        return None

# Test 1: Health Check Endpoint Test
def test_health_endpoint(base_url):
    url = base_url + "/"
    response = requests.get(url)
    assert response.status_code == 200, "Health endpoint did not return a 200 status code"
    print("Health Check Endpoint Test passed")

# Test 2: Index.html Content Test
def test_index_html_content(base_url):
    url = base_url + "/"
    response = requests.get(url)
    with open("/home/ec2-user/interviews/html/index.html", 'r') as file:
        file_content = file.read()
    assert file_content in response.text, "Index.html content does not match expected content"
    print("Index.html Content Test passed")

# Test 3: Ingress Test
def test_ingress(ingress_url):
    response = requests.get(ingress_url)
    assert response.status_code == 200, "Failed to access Ingress endpoint"
    print("Ingress Test passed")

# Test 4: End-to-End Test
def test_end_to_end(base_url):
    test_health_endpoint(base_url)
    test_index_html_content(base_url)
    test_number_of_pods()
    print("End-to-End Test passed")

# Test 5: Number of pods Test
def test_number_of_pods():
    # Get the number of pods for the deployment
    number_of_pods = get_number_of_pods()
    if number_of_pods is not None:
        # Add assertion here to validate the number of pods
        assert number_of_pods >= 2, f"Number of pods for deployment is not as expected"
        assert number_of_pods <= 4, f"Number of pods for deployment is not as expected"
        print("Number_of_pods Test passed")
    else:
        print("Number_of_pods Test failed")

if __name__ == "__main__":
    base_url = "http://a0fc6e44e91354ebd80c124364b6b228-1053065812.us-west-2.elb.amazonaws.com"
    ingress_url = "http://httpd-shivamgaur.ping-fuji.com"

    test_health_endpoint(base_url)
    test_index_html_content(base_url)
    test_ingress(ingress_url)
    test_number_of_pods()
    test_end_to_end(base_url)
