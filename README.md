# transcription_service
Requirements:

python3 (version higher or equal to 3.7, at least 3.9 is recommended)
ffmpeg (see instructions for installation on the whisper repository)

You can install whisper-timestamped either by using pip:

pip3 install git+https://github.com/linto-ai/whisper-timestamped
or by cloning this repository and running installation:

git clone https://github.com/linto-ai/whisper-timestamped
cd whisper-timestamped/
python3 setup.py install
Additional packages that might be needed
If you want to plot alignment between audio timestamps and words (as in this section), you also need matplotlib:

pip3 install matplotlib
If you want to use VAD option (Voice Activity Detection before running Whisper model), you also need torchaudio and onnxruntime:

pip3 install onnxruntime torchaudio
If you want to use finetuned Whisper models from the Hugging Face Hub, you also need transformers:

pip3 install transformers
Docker
A docker image of about 9GB can be built using:

git clone https://github.com/linto-ai/whisper-timestamped
cd whisper-timestamped/
docker build -t whisper_timestamped:latest .
Light installation for CPU
If you don't have a GPU (or don't want to use it), then you don't need to install the CUDA dependencies. You should then just install a light version of torch before installing whisper-timestamped, for instance as follows:

pip3 install \
     torch==1.13.1+cpu \
     torchaudio==0.13.1+cpu \
     -f https://download.pytorch.org/whl/torch_stable.html
A specific docker image of about 3.5GB can also be built using:

git clone https://github.com/linto-ai/whisper-timestamped
cd whisper-timestamped/
docker build -t whisper_timestamped_cpu:latest -f Dockerfile.cpu .
Upgrade to the latest version
When using pip, the library can be updated to the latest version using:

pip3 install --upgrade --no-deps --force-reinstall git+https://github.com/linto-ai/whisper-timestamped
A specific version of openai-whisper can be used by running, for example:

pip3 install openai-whisper==20230124
