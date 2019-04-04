from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='MaskRCNN',
    author='Leixin Zhou',
    url='github.com/leixinzhou/MaskRCNN',
    packages=['mrcnn'],
    ext_modules=[
        CUDAExtension('mrcnn.models.components.nms.nms_wrapper', [
            './mrcnn/models/components/nms/nms_wrapper.cpp',
            './mrcnn/models/components/nms/nms_cuda.cu',
        ]),
        CUDAExtension('mrcnn.models.components.roialign.crop_and_resize', [
            './mrcnn/models/components/roialign/crop_and_resize_gpu.cpp',
            './mrcnn/models/components/roialign/crop_and_resize_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
})