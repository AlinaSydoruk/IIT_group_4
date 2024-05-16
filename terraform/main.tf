provider "aws" {
  region = "us-east-1"
}

resource "aws_lightsail_instance" "my_ubuntu_instance" {
  name              = "UbuntuInstance"
  availability_zone = "us-east-1a"
  blueprint_id      = "ubuntu_20_04"
  bundle_id         = "nano_2_0"

  tags = {
    Name = "UbuntuInstance"
  }
}

output "public_ip" {
  value = aws_lightsail_instance.my_ubuntu_instance.public_ip_address
}
