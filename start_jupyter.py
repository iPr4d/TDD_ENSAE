import os
import subprocess
import sys
import logging

if __name__ == '__main__':

    USERNAME = os.popen('ls /home').read().replace('\n', '')

    user_directory = f'/home/{USERNAME}'

    env = os.environ # Get current environment

    # Install java if needed
    cmd_check_java = ['java', '-version']
    try: 
        subprocess.check_output(cmd_check_java, stderr=subprocess.STDOUT)
        logging.info('Java already installed')
    except FileNotFoundError:
        cmd_java_installation = ["sudo", "apt", "install", "default-jdk"]
        p = subprocess.Popen(cmd_java_installation, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        p.stdin.write(b"y\n")        
        outputlog, errorlog = p.communicate()

    # Add JAVA_HOME to environment variables
    env['JAVA_HOME'] = '/usr/lib/jvm/java-11-openjdk-amd64'

    # Create spark-hadoop directory
    try:
        os.mkdir(f'{user_directory}/spark-hadoop')
    except FileExistsError:
        logging.info('Directory spark-hadoop already exists.')

    # Download Spark
    if len(os.listdir(f'{user_directory}/spark-hadoop')) == 0 : # avoid downloading if already done (quite long)  
        os.chdir(f'{user_directory}/spark-hadoop')
        os.system('wget https://downloads.apache.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz')
        logging.info('Spark succesfully downloaded.')
    else:
        logging.info('Spark already downloaded... \nTrying to decompress it if not already done.')

    # Decompress Spark archive
    if not 'spark-2.4.5-bin-hadoop2.7' in os.listdir(f'{user_directory}/spark-hadoop'):
        os.chdir(f'{user_directory}/spark-hadoop')
        os.system(f'tar -xvf {user_directory}/spark-hadoop/spark-2.4.5-bin-hadoop2.7.tgz')
        logging.info('Spark unzipped succesfully')
    else: 
        logging.info('Spark already decompressed.')

    # Add SPARK_HOME to environment variables and PATH
    SPARK_HOME = f"{user_directory}/spark-hadoop/spark-2.4.5-bin-hadoop2.7"
    env['SPARK_HOME'] = SPARK_HOME

    os.chdir('/root')
    os.system('mkdir tmp')
    os.chdir('/root/tmp')

    # Download Anaconda for Linux OS
    os.system('wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh')

    # Install anaconda3
    cmd_conda_install = ['bash', 'Anaconda3-2020.02-Linux-x86_64.sh']
    p = subprocess.Popen(cmd_conda_install, stdin=subprocess.PIPE, stdout=subprocess.PIPE, cwd='/root/tmp')
    p.stdin.write(b"\n")
    p.stdin.write(b"yes")
    p.stdin.write(b"\n")
    outputlog, errorlog = p.communicate()

    # Add anaconda3 and spark to PATH
    env['PATH'] = f'{SPARK_HOME}/bin:{SPARK_HOME}/sbin:'+env['PATH']
    env['PATH'] = "/root/anaconda3/bin:"+env['PATH']

    # Install pyspark
    os.system("conda install -c conda-forge pyspark")

    # Start a notebook openable in host browser (use given url with token)
    os.system('jupyter notebook --allow-root --no-browser --port 8004 --ip=0.0.0.0')

