"""                                                                                                      
Copyright 2016-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.                                  
                                                                                                         
Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at                                              
                                                                                                         
    http://aws.amazon.com/apache2.0/                                                                     
                                                                                                         
or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.                                                 
"""

from . import flip
import click
import sys

@click.command()
@click.option("--json", "-j", "out_format", flag_value="json", help="Convert to JSON. Assume the input is YAML.")
@click.option("--yaml", "-y", "out_format", flag_value="yaml", help="Convert to YAML. Assume the input is JSON.")
@click.option("--no-flip", "-n", is_flag=True, help="Don't convert. You can use this to validate or just clean a template without converting it. If you use -n in conjunction with -j or -y, the input format is assumed to be the same as the output format you specify.")
@click.option("--clean", "-c", is_flag=True, help="Performs some opinionated cleanup on your template. For now, this just converts uses of Fn::Join to Fn::Sub.")
@click.argument("input", type=click.File("r"), default=sys.stdin)
@click.argument("output", type=click.File("w"), default=sys.stdout)
def main(out_format, no_flip, clean, input, output):
    """
    AWS CloudFormation Template Flip is a tool that converts
    AWS CloudFormation templates between JSON and YAML formats,
    making use of the YAML format's short function syntax where possible."
    """

    try:
        output.write(flip(input.read(),
            out_format=out_format,
            clean_up=clean,
            no_flip=no_flip
        ))
    except Exception as e:
        raise click.ClickException("{}".format(e))
