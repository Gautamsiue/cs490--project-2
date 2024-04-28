
rm -rf ../miniconda3
if [ ! -d "../miniconda3" ]; then
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh

    echo 'export PATH="~/miniconda/bin:$PATH"' >> ~/.bashrc

    source ~/.bashrc

    source ~/miniconda3/etc/profile.d/conda.sh

    
    read -p "Name the env: " name
    read -p " python : " ver
    conda create --name $name python=$ver
    conda activate $name
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cpuonly -c pytorch
    conda install numpy
fi
