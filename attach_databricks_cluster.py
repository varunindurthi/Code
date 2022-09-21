# ------------------------------------------------------
# Attach the Databricks Cluster to the AzureML Workspace
# as an Attached Compute
# ------------------------------------------------------

from azureml.core import Workspace
from azureml.core.compute import DatabricksCompute, ComputeTarget
import yaml

# Access the Workspace
print("Accessing the AzureML workspace...")
ws = Workspace.from_config("./config")


# Create the configuration information of the cluster
print("Initializing the parameters...")
credentials = yaml.load(open('./credentials.yml'))
db_resource_group     = credentials['db']['db_resource_group']
db_workspace_name     = credentials['db']['db_workspace_name']
db_access_token       = credentials['db']['db_access_token']
db_compute_name       = credentials['db']['db_compute_name']

if db_compute_name not in ws.compute_targets:
    print("Creating Configuration for the DB Cluster....")
    attach_config = DatabricksCompute.attach_configuration(
                                resource_group = db_resource_group,
                                workspace_name = db_workspace_name,
                                access_token = db_access_token)
    
    print("Attaching the compute target....")
    db_cluster = ComputeTarget.attach(ws, 
                                      db_compute_name, 
                                      attach_config)
    
    db_cluster.wait_for_completion(True)

else:
    print("Compute target exists...")
    db_cluster = ws.compute_targets[db_compute_name]


















