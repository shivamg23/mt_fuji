# Mt Fuji Interview Process Submission - Mt. Fuji

This is a take-home programming assignment that I completed as part of the Ping Identity interview process. This README provides instructions for setting up an interview environment using Kubernetes and AWS Route 53.

## Getting Started

This README provides instructions for setting up an environment using Kubernetes and AWS Route 53.

## Prerequisities

In order to run this, you'll need python, aws-cli installed.


## Usage

1. Navigate to the `interviews` directory:
    cd ~/interviews

2. Create a ConfigMap named `html-conf` using the HTML files located in the `html` directory:
    kubectl create configmap html-conf --from-file=./html

3. Apply the Kubernetes deployment configuration:
    kubectl apply -f deploy.yaml

4. Obtain the LoadBalancer ingress by running:
    kubectl describe svc

5. Update the obtained ingress URL in the following files:
- `interviews/tst/tests.py` -> `base_url`
- `interviews/misc/patch.json` -> `DNS name`

6. To create, update, or delete DNS records in a hosted zone, use the following AWS CLI command:
    aws route53 change-resource-record-sets --hosted-zone-id <hosted-zone-id> --change-batch file://misc/patch.json

7. Execute the Python testCase file:
    python3 interviews/tst/tests.py

8. The final required html file can be accessed through httpd-shivamgaur.ping-fuji.com.


On your local machine, clone this repo:

```shell
git clone --recursive https://github.com/shivamg23/mt_fuji.git
cd interviews

## Authors

* **Shivam Gaur** - [Email](shivam.gaur2019@gmail.com)

## Acknowledgments

* [Ping Identity: Identity Security for the Digital Enterprise](https://www.pingidentity.com)
* [AWS Documentation](https://docs.aws.amazon.com/)
