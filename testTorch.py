import torch

# Check if CUDA is available
if torch.cuda.is_available():
    # Get the PyTorch version
    torch_version = torch.__version__
    print(f"PyTorch version: {torch_version}")

    # Get the CUDA version supported by PyTorch
    cuda_version = torch.version.cuda
    print(f"PyTorch is built with CUDA version: {cuda_version}")

    # Get the CUDA runtime version on your system
    cuda_runtime_version = torch.cuda.get_device_capability()
    print(f"CUDA runtime version on your system: {cuda_runtime_version}")

    # Check if the CUDA versions are compatible
    if cuda_version:
        print(f"PyTorch and CUDA are compatible. PyTorch is built with CUDA version {cuda_version}, and your system has CUDA runtime version {cuda_runtime_version}.")
    else:
        print("PyTorch is built without CUDA support.")
else:
    print("CUDA is not available in your PyTorch installation.")
