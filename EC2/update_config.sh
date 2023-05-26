#! /bin/bash



# define the file path and the field to be modified
conf_file_path="/etc/mongod.conf"
field_to_modify="bindIp"

# define the new value you want to set for the field
new_value="0.0.0.0"

# use sed to find and replace the value
sudo sed -i "s/^${field_to_modify}:.*$/${field_to_modify}: ${new_value}/" $conf_file_path