from azureml.core import Workspace, Datastore

ws = Workspace.from_config(path='./config/')

az_store = Datastore.register_azure_blob_container(workspace=ws,
                                                   datastore_name='azureml_ds_practice_01',
                                                   account_name='amlpractice',
                                                   container_name='azuremlpracticeblob',
                                                   account_key='mpLs3ar9+iTj+ndxPVE6rgAUkYSYEi1xyYZY5rnmjILa1zvyf+Vz/+zw+ycELf2FiJ/cfJP3F/Ib+ASt/Y3/Lg=='
                                                   )