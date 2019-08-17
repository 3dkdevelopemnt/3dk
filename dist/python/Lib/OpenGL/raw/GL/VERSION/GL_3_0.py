'''OpenGL extension VERSION.GL_3_0

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_3_0'
_DEPRECATED = False
GL_COMPARE_REF_TO_TEXTURE = constant.Constant( 'GL_COMPARE_REF_TO_TEXTURE', 0x884E )
GL_CLIP_DISTANCE0 = constant.Constant( 'GL_CLIP_DISTANCE0', 0x3000 )
GL_CLIP_DISTANCE1 = constant.Constant( 'GL_CLIP_DISTANCE1', 0x3001 )
GL_CLIP_DISTANCE2 = constant.Constant( 'GL_CLIP_DISTANCE2', 0x3002 )
GL_CLIP_DISTANCE3 = constant.Constant( 'GL_CLIP_DISTANCE3', 0x3003 )
GL_CLIP_DISTANCE4 = constant.Constant( 'GL_CLIP_DISTANCE4', 0x3004 )
GL_CLIP_DISTANCE5 = constant.Constant( 'GL_CLIP_DISTANCE5', 0x3005 )
GL_CLIP_DISTANCE6 = constant.Constant( 'GL_CLIP_DISTANCE6', 0x3006 )
GL_CLIP_DISTANCE7 = constant.Constant( 'GL_CLIP_DISTANCE7', 0x3007 )
GL_MAX_CLIP_DISTANCES = constant.Constant( 'GL_MAX_CLIP_DISTANCES', 0xD32 )
GL_MAJOR_VERSION = constant.Constant( 'GL_MAJOR_VERSION', 0x821B )
GL_MINOR_VERSION = constant.Constant( 'GL_MINOR_VERSION', 0x821C )
GL_NUM_EXTENSIONS = constant.Constant( 'GL_NUM_EXTENSIONS', 0x821D )
GL_CONTEXT_FLAGS = constant.Constant( 'GL_CONTEXT_FLAGS', 0x821E )
GL_DEPTH_BUFFER = constant.Constant( 'GL_DEPTH_BUFFER', 0x8223 )
GL_STENCIL_BUFFER = constant.Constant( 'GL_STENCIL_BUFFER', 0x8224 )
GL_COMPRESSED_RED = constant.Constant( 'GL_COMPRESSED_RED', 0x8225 )
GL_COMPRESSED_RG = constant.Constant( 'GL_COMPRESSED_RG', 0x8226 )
GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT = constant.Constant( 'GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT', 0x1 )
GL_RGBA32F = constant.Constant( 'GL_RGBA32F', 0x8814 )
GL_RGB32F = constant.Constant( 'GL_RGB32F', 0x8815 )
GL_RGBA16F = constant.Constant( 'GL_RGBA16F', 0x881A )
GL_RGB16F = constant.Constant( 'GL_RGB16F', 0x881B )
GL_VERTEX_ATTRIB_ARRAY_INTEGER = constant.Constant( 'GL_VERTEX_ATTRIB_ARRAY_INTEGER', 0x88FD )
GL_MAX_ARRAY_TEXTURE_LAYERS = constant.Constant( 'GL_MAX_ARRAY_TEXTURE_LAYERS', 0x88FF )
GL_MIN_PROGRAM_TEXEL_OFFSET = constant.Constant( 'GL_MIN_PROGRAM_TEXEL_OFFSET', 0x8904 )
GL_MAX_PROGRAM_TEXEL_OFFSET = constant.Constant( 'GL_MAX_PROGRAM_TEXEL_OFFSET', 0x8905 )
GL_CLAMP_READ_COLOR = constant.Constant( 'GL_CLAMP_READ_COLOR', 0x891C )
GL_FIXED_ONLY = constant.Constant( 'GL_FIXED_ONLY', 0x891D )
GL_MAX_VARYING_COMPONENTS = constant.Constant( 'GL_MAX_VARYING_COMPONENTS', 0x8B4B )
GL_TEXTURE_1D_ARRAY = constant.Constant( 'GL_TEXTURE_1D_ARRAY', 0x8C18 )
GL_PROXY_TEXTURE_1D_ARRAY = constant.Constant( 'GL_PROXY_TEXTURE_1D_ARRAY', 0x8C19 )
GL_TEXTURE_2D_ARRAY = constant.Constant( 'GL_TEXTURE_2D_ARRAY', 0x8C1A )
GL_PROXY_TEXTURE_2D_ARRAY = constant.Constant( 'GL_PROXY_TEXTURE_2D_ARRAY', 0x8C1B )
GL_TEXTURE_BINDING_1D_ARRAY = constant.Constant( 'GL_TEXTURE_BINDING_1D_ARRAY', 0x8C1C )
GL_TEXTURE_BINDING_2D_ARRAY = constant.Constant( 'GL_TEXTURE_BINDING_2D_ARRAY', 0x8C1D )
GL_R11F_G11F_B10F = constant.Constant( 'GL_R11F_G11F_B10F', 0x8C3A )
GL_UNSIGNED_INT_10F_11F_11F_REV = constant.Constant( 'GL_UNSIGNED_INT_10F_11F_11F_REV', 0x8C3B )
GL_RGB9_E5 = constant.Constant( 'GL_RGB9_E5', 0x8C3D )
GL_UNSIGNED_INT_5_9_9_9_REV = constant.Constant( 'GL_UNSIGNED_INT_5_9_9_9_REV', 0x8C3E )
GL_TEXTURE_SHARED_SIZE = constant.Constant( 'GL_TEXTURE_SHARED_SIZE', 0x8C3F )
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = constant.Constant( 'GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH', 0x8C76 )
GL_TRANSFORM_FEEDBACK_BUFFER_MODE = constant.Constant( 'GL_TRANSFORM_FEEDBACK_BUFFER_MODE', 0x8C7F )
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = constant.Constant( 'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS', 0x8C80 )
GL_TRANSFORM_FEEDBACK_VARYINGS = constant.Constant( 'GL_TRANSFORM_FEEDBACK_VARYINGS', 0x8C83 )
GL_TRANSFORM_FEEDBACK_BUFFER_START = constant.Constant( 'GL_TRANSFORM_FEEDBACK_BUFFER_START', 0x8C84 )
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = constant.Constant( 'GL_TRANSFORM_FEEDBACK_BUFFER_SIZE', 0x8C85 )
GL_PRIMITIVES_GENERATED = constant.Constant( 'GL_PRIMITIVES_GENERATED', 0x8C87 )
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = constant.Constant( 'GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN', 0x8C88 )
GL_RASTERIZER_DISCARD = constant.Constant( 'GL_RASTERIZER_DISCARD', 0x8C89 )
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = constant.Constant( 'GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS', 0x8C8A )
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = constant.Constant( 'GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS', 0x8C8B )
GL_INTERLEAVED_ATTRIBS = constant.Constant( 'GL_INTERLEAVED_ATTRIBS', 0x8C8C )
GL_SEPARATE_ATTRIBS = constant.Constant( 'GL_SEPARATE_ATTRIBS', 0x8C8D )
GL_TRANSFORM_FEEDBACK_BUFFER = constant.Constant( 'GL_TRANSFORM_FEEDBACK_BUFFER', 0x8C8E )
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = constant.Constant( 'GL_TRANSFORM_FEEDBACK_BUFFER_BINDING', 0x8C8F )
GL_RGBA32UI = constant.Constant( 'GL_RGBA32UI', 0x8D70 )
GL_RGB32UI = constant.Constant( 'GL_RGB32UI', 0x8D71 )
GL_RGBA16UI = constant.Constant( 'GL_RGBA16UI', 0x8D76 )
GL_RGB16UI = constant.Constant( 'GL_RGB16UI', 0x8D77 )
GL_RGBA8UI = constant.Constant( 'GL_RGBA8UI', 0x8D7C )
GL_RGB8UI = constant.Constant( 'GL_RGB8UI', 0x8D7D )
GL_RGBA32I = constant.Constant( 'GL_RGBA32I', 0x8D82 )
GL_RGB32I = constant.Constant( 'GL_RGB32I', 0x8D83 )
GL_RGBA16I = constant.Constant( 'GL_RGBA16I', 0x8D88 )
GL_RGB16I = constant.Constant( 'GL_RGB16I', 0x8D89 )
GL_RGBA8I = constant.Constant( 'GL_RGBA8I', 0x8D8E )
GL_RGB8I = constant.Constant( 'GL_RGB8I', 0x8D8F )
GL_RED_INTEGER = constant.Constant( 'GL_RED_INTEGER', 0x8D94 )
GL_GREEN_INTEGER = constant.Constant( 'GL_GREEN_INTEGER', 0x8D95 )
GL_BLUE_INTEGER = constant.Constant( 'GL_BLUE_INTEGER', 0x8D96 )
GL_RGB_INTEGER = constant.Constant( 'GL_RGB_INTEGER', 0x8D98 )
GL_RGBA_INTEGER = constant.Constant( 'GL_RGBA_INTEGER', 0x8D99 )
GL_BGR_INTEGER = constant.Constant( 'GL_BGR_INTEGER', 0x8D9A )
GL_BGRA_INTEGER = constant.Constant( 'GL_BGRA_INTEGER', 0x8D9B )
GL_SAMPLER_1D_ARRAY = constant.Constant( 'GL_SAMPLER_1D_ARRAY', 0x8DC0 )
GL_SAMPLER_2D_ARRAY = constant.Constant( 'GL_SAMPLER_2D_ARRAY', 0x8DC1 )
GL_SAMPLER_1D_ARRAY_SHADOW = constant.Constant( 'GL_SAMPLER_1D_ARRAY_SHADOW', 0x8DC3 )
GL_SAMPLER_2D_ARRAY_SHADOW = constant.Constant( 'GL_SAMPLER_2D_ARRAY_SHADOW', 0x8DC4 )
GL_SAMPLER_CUBE_SHADOW = constant.Constant( 'GL_SAMPLER_CUBE_SHADOW', 0x8DC5 )
GL_UNSIGNED_INT_VEC2 = constant.Constant( 'GL_UNSIGNED_INT_VEC2', 0x8DC6 )
GL_UNSIGNED_INT_VEC3 = constant.Constant( 'GL_UNSIGNED_INT_VEC3', 0x8DC7 )
GL_UNSIGNED_INT_VEC4 = constant.Constant( 'GL_UNSIGNED_INT_VEC4', 0x8DC8 )
GL_INT_SAMPLER_1D = constant.Constant( 'GL_INT_SAMPLER_1D', 0x8DC9 )
GL_INT_SAMPLER_2D = constant.Constant( 'GL_INT_SAMPLER_2D', 0x8DCA )
GL_INT_SAMPLER_3D = constant.Constant( 'GL_INT_SAMPLER_3D', 0x8DCB )
GL_INT_SAMPLER_CUBE = constant.Constant( 'GL_INT_SAMPLER_CUBE', 0x8DCC )
GL_INT_SAMPLER_1D_ARRAY = constant.Constant( 'GL_INT_SAMPLER_1D_ARRAY', 0x8DCE )
GL_INT_SAMPLER_2D_ARRAY = constant.Constant( 'GL_INT_SAMPLER_2D_ARRAY', 0x8DCF )
GL_UNSIGNED_INT_SAMPLER_1D = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_1D', 0x8DD1 )
GL_UNSIGNED_INT_SAMPLER_2D = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_2D', 0x8DD2 )
GL_UNSIGNED_INT_SAMPLER_3D = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_3D', 0x8DD3 )
GL_UNSIGNED_INT_SAMPLER_CUBE = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_CUBE', 0x8DD4 )
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_1D_ARRAY', 0x8DD6 )
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = constant.Constant( 'GL_UNSIGNED_INT_SAMPLER_2D_ARRAY', 0x8DD7 )
GL_QUERY_WAIT = constant.Constant( 'GL_QUERY_WAIT', 0x8E13 )
GL_QUERY_NO_WAIT = constant.Constant( 'GL_QUERY_NO_WAIT', 0x8E14 )
GL_QUERY_BY_REGION_WAIT = constant.Constant( 'GL_QUERY_BY_REGION_WAIT', 0x8E15 )
GL_QUERY_BY_REGION_NO_WAIT = constant.Constant( 'GL_QUERY_BY_REGION_NO_WAIT', 0x8E16 )
GL_BUFFER_ACCESS_FLAGS = constant.Constant( 'GL_BUFFER_ACCESS_FLAGS', 0x911F )
GL_BUFFER_MAP_LENGTH = constant.Constant( 'GL_BUFFER_MAP_LENGTH', 0x9120 )
GL_BUFFER_MAP_OFFSET = constant.Constant( 'GL_BUFFER_MAP_OFFSET', 0x9121 )
glColorMaski = platform.createExtensionFunction( 
'glColorMaski',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLboolean,constants.GLboolean,constants.GLboolean,constants.GLboolean,),
doc='glColorMaski(GLuint(index), GLboolean(r), GLboolean(g), GLboolean(b), GLboolean(a)) -> None',
argNames=('index','r','g','b','a',),
deprecated=_DEPRECATED,
)

glGetBooleani_v = platform.createExtensionFunction( 
'glGetBooleani_v',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,arrays.GLbooleanArray,),
doc='glGetBooleani_v(GLenum(target), GLuint(index), GLbooleanArray(data)) -> None',
argNames=('target','index','data',),
deprecated=_DEPRECATED,
)

glGetIntegeri_v = platform.createExtensionFunction( 
'glGetIntegeri_v',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,arrays.GLintArray,),
doc='glGetIntegeri_v(GLenum(target), GLuint(index), GLintArray(data)) -> None',
argNames=('target','index','data',),
deprecated=_DEPRECATED,
)

glEnablei = platform.createExtensionFunction( 
'glEnablei',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,),
doc='glEnablei(GLenum(target), GLuint(index)) -> None',
argNames=('target','index',),
deprecated=_DEPRECATED,
)

glDisablei = platform.createExtensionFunction( 
'glDisablei',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,),
doc='glDisablei(GLenum(target), GLuint(index)) -> None',
argNames=('target','index',),
deprecated=_DEPRECATED,
)

glIsEnabledi = platform.createExtensionFunction( 
'glIsEnabledi',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLboolean, 
argTypes=(constants.GLenum,constants.GLuint,),
doc='glIsEnabledi(GLenum(target), GLuint(index)) -> constants.GLboolean',
argNames=('target','index',),
deprecated=_DEPRECATED,
)

glBeginTransformFeedback = platform.createExtensionFunction( 
'glBeginTransformFeedback',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,),
doc='glBeginTransformFeedback(GLenum(primitiveMode)) -> None',
argNames=('primitiveMode',),
deprecated=_DEPRECATED,
)

glEndTransformFeedback = platform.createExtensionFunction( 
'glEndTransformFeedback',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(),
doc='glEndTransformFeedback() -> None',
argNames=(),
deprecated=_DEPRECATED,
)

glBindBufferRange = platform.createExtensionFunction( 
'glBindBufferRange',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,constants.GLuint,constants.GLintptr,constants.GLsizeiptr,),
doc='glBindBufferRange(GLenum(target), GLuint(index), GLuint(buffer), GLintptr(offset), GLsizeiptr(size)) -> None',
argNames=('target','index','buffer','offset','size',),
deprecated=_DEPRECATED,
)

glBindBufferBase = platform.createExtensionFunction( 
'glBindBufferBase',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLuint,constants.GLuint,),
doc='glBindBufferBase(GLenum(target), GLuint(index), GLuint(buffer)) -> None',
argNames=('target','index','buffer',),
deprecated=_DEPRECATED,
)

glTransformFeedbackVaryings = platform.createExtensionFunction( 
'glTransformFeedbackVaryings',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLsizei,ctypes.POINTER( ctypes.POINTER( constants.GLchar )),constants.GLenum,),
doc='glTransformFeedbackVaryings(GLuint(program), GLsizei(count), POINTER( ctypes.POINTER( constants.GLchar ))(varyings), GLenum(bufferMode)) -> None',
argNames=('program','count','varyings','bufferMode',),
deprecated=_DEPRECATED,
)

glGetTransformFeedbackVarying = platform.createExtensionFunction( 
'glGetTransformFeedbackVarying',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLsizei,arrays.GLsizeiArray,arrays.GLsizeiArray,arrays.GLuintArray,arrays.GLcharArray,),
doc='glGetTransformFeedbackVarying(GLuint(program), GLuint(index), GLsizei(bufSize), GLsizeiArray(length), GLsizeiArray(size), GLuintArray(type), GLcharArray(name)) -> None',
argNames=('program','index','bufSize','length','size','type','name',),
deprecated=_DEPRECATED,
)

glClampColor = platform.createExtensionFunction( 
'glClampColor',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,),
doc='glClampColor(GLenum(target), GLenum(clamp)) -> None',
argNames=('target','clamp',),
deprecated=_DEPRECATED,
)

glBeginConditionalRender = platform.createExtensionFunction( 
'glBeginConditionalRender',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,),
doc='glBeginConditionalRender(GLuint(id), GLenum(mode)) -> None',
argNames=('id','mode',),
deprecated=_DEPRECATED,
)

glEndConditionalRender = platform.createExtensionFunction( 
'glEndConditionalRender',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(),
doc='glEndConditionalRender() -> None',
argNames=(),
deprecated=_DEPRECATED,
)

glVertexAttribIPointer = platform.createExtensionFunction( 
'glVertexAttribIPointer',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLenum,constants.GLsizei,ctypes.c_void_p,),
doc='glVertexAttribIPointer(GLuint(index), GLint(size), GLenum(type), GLsizei(stride), c_void_p(pointer)) -> None',
argNames=('index','size','type','stride','pointer',),
deprecated=_DEPRECATED,
)

glGetVertexAttribIiv = platform.createExtensionFunction( 
'glGetVertexAttribIiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLintArray,),
doc='glGetVertexAttribIiv(GLuint(index), GLenum(pname), GLintArray(params)) -> None',
argNames=('index','pname','params',),
deprecated=_DEPRECATED,
)

glGetVertexAttribIuiv = platform.createExtensionFunction( 
'glGetVertexAttribIuiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,arrays.GLuintArray,),
doc='glGetVertexAttribIuiv(GLuint(index), GLenum(pname), GLuintArray(params)) -> None',
argNames=('index','pname','params',),
deprecated=_DEPRECATED,
)

glVertexAttribI1i = platform.createExtensionFunction( 
'glVertexAttribI1i',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,),
doc='glVertexAttribI1i(GLuint(index), GLint(x)) -> None',
argNames=('index','x',),
deprecated=_DEPRECATED,
)

glVertexAttribI2i = platform.createExtensionFunction( 
'glVertexAttribI2i',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLint,),
doc='glVertexAttribI2i(GLuint(index), GLint(x), GLint(y)) -> None',
argNames=('index','x','y',),
deprecated=_DEPRECATED,
)

glVertexAttribI3i = platform.createExtensionFunction( 
'glVertexAttribI3i',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLint,constants.GLint,),
doc='glVertexAttribI3i(GLuint(index), GLint(x), GLint(y), GLint(z)) -> None',
argNames=('index','x','y','z',),
deprecated=_DEPRECATED,
)

glVertexAttribI4i = platform.createExtensionFunction( 
'glVertexAttribI4i',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,constants.GLint,constants.GLint,constants.GLint,),
doc='glVertexAttribI4i(GLuint(index), GLint(x), GLint(y), GLint(z), GLint(w)) -> None',
argNames=('index','x','y','z','w',),
deprecated=_DEPRECATED,
)

glVertexAttribI1ui = platform.createExtensionFunction( 
'glVertexAttribI1ui',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,),
doc='glVertexAttribI1ui(GLuint(index), GLuint(x)) -> None',
argNames=('index','x',),
deprecated=_DEPRECATED,
)

glVertexAttribI2ui = platform.createExtensionFunction( 
'glVertexAttribI2ui',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glVertexAttribI2ui(GLuint(index), GLuint(x), GLuint(y)) -> None',
argNames=('index','x','y',),
deprecated=_DEPRECATED,
)

glVertexAttribI3ui = platform.createExtensionFunction( 
'glVertexAttribI3ui',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glVertexAttribI3ui(GLuint(index), GLuint(x), GLuint(y), GLuint(z)) -> None',
argNames=('index','x','y','z',),
deprecated=_DEPRECATED,
)

glVertexAttribI4ui = platform.createExtensionFunction( 
'glVertexAttribI4ui',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glVertexAttribI4ui(GLuint(index), GLuint(x), GLuint(y), GLuint(z), GLuint(w)) -> None',
argNames=('index','x','y','z','w',),
deprecated=_DEPRECATED,
)

glVertexAttribI1iv = platform.createExtensionFunction( 
'glVertexAttribI1iv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLintArray,),
doc='glVertexAttribI1iv(GLuint(index), GLintArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI2iv = platform.createExtensionFunction( 
'glVertexAttribI2iv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLintArray,),
doc='glVertexAttribI2iv(GLuint(index), GLintArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI3iv = platform.createExtensionFunction( 
'glVertexAttribI3iv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLintArray,),
doc='glVertexAttribI3iv(GLuint(index), GLintArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI4iv = platform.createExtensionFunction( 
'glVertexAttribI4iv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLintArray,),
doc='glVertexAttribI4iv(GLuint(index), GLintArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI1uiv = platform.createExtensionFunction( 
'glVertexAttribI1uiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLuintArray,),
doc='glVertexAttribI1uiv(GLuint(index), GLuintArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI2uiv = platform.createExtensionFunction( 
'glVertexAttribI2uiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLuintArray,),
doc='glVertexAttribI2uiv(GLuint(index), GLuintArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI3uiv = platform.createExtensionFunction( 
'glVertexAttribI3uiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLuintArray,),
doc='glVertexAttribI3uiv(GLuint(index), GLuintArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI4uiv = platform.createExtensionFunction( 
'glVertexAttribI4uiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLuintArray,),
doc='glVertexAttribI4uiv(GLuint(index), GLuintArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI4bv = platform.createExtensionFunction( 
'glVertexAttribI4bv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLbyteArray,),
doc='glVertexAttribI4bv(GLuint(index), GLbyteArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI4sv = platform.createExtensionFunction( 
'glVertexAttribI4sv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLshortArray,),
doc='glVertexAttribI4sv(GLuint(index), GLshortArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI4ubv = platform.createExtensionFunction( 
'glVertexAttribI4ubv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLubyteArray,),
doc='glVertexAttribI4ubv(GLuint(index), GLubyteArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glVertexAttribI4usv = platform.createExtensionFunction( 
'glVertexAttribI4usv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,arrays.GLushortArray,),
doc='glVertexAttribI4usv(GLuint(index), GLushortArray(v)) -> None',
argNames=('index','v',),
deprecated=_DEPRECATED,
)

glGetUniformuiv = platform.createExtensionFunction( 
'glGetUniformuiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLint,arrays.GLuintArray,),
doc='glGetUniformuiv(GLuint(program), GLint(location), GLuintArray(params)) -> None',
argNames=('program','location','params',),
deprecated=_DEPRECATED,
)

glBindFragDataLocation = platform.createExtensionFunction( 
'glBindFragDataLocation',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLuint,arrays.GLcharArray,),
doc='glBindFragDataLocation(GLuint(program), GLuint(color), GLcharArray(name)) -> None',
argNames=('program','color','name',),
deprecated=_DEPRECATED,
)

glGetFragDataLocation = platform.createExtensionFunction( 
'glGetFragDataLocation',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=constants.GLint, 
argTypes=(constants.GLuint,arrays.GLcharArray,),
doc='glGetFragDataLocation(GLuint(program), GLcharArray(name)) -> constants.GLint',
argNames=('program','name',),
deprecated=_DEPRECATED,
)

glUniform1ui = platform.createExtensionFunction( 
'glUniform1ui',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLuint,),
doc='glUniform1ui(GLint(location), GLuint(v0)) -> None',
argNames=('location','v0',),
deprecated=_DEPRECATED,
)

glUniform2ui = platform.createExtensionFunction( 
'glUniform2ui',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLuint,constants.GLuint,),
doc='glUniform2ui(GLint(location), GLuint(v0), GLuint(v1)) -> None',
argNames=('location','v0','v1',),
deprecated=_DEPRECATED,
)

glUniform3ui = platform.createExtensionFunction( 
'glUniform3ui',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glUniform3ui(GLint(location), GLuint(v0), GLuint(v1), GLuint(v2)) -> None',
argNames=('location','v0','v1','v2',),
deprecated=_DEPRECATED,
)

glUniform4ui = platform.createExtensionFunction( 
'glUniform4ui',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLuint,constants.GLuint,constants.GLuint,constants.GLuint,),
doc='glUniform4ui(GLint(location), GLuint(v0), GLuint(v1), GLuint(v2), GLuint(v3)) -> None',
argNames=('location','v0','v1','v2','v3',),
deprecated=_DEPRECATED,
)

glUniform1uiv = platform.createExtensionFunction( 
'glUniform1uiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLuintArray,),
doc='glUniform1uiv(GLint(location), GLsizei(count), GLuintArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniform2uiv = platform.createExtensionFunction( 
'glUniform2uiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLuintArray,),
doc='glUniform2uiv(GLint(location), GLsizei(count), GLuintArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniform3uiv = platform.createExtensionFunction( 
'glUniform3uiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLuintArray,),
doc='glUniform3uiv(GLint(location), GLsizei(count), GLuintArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glUniform4uiv = platform.createExtensionFunction( 
'glUniform4uiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLint,constants.GLsizei,arrays.GLuintArray,),
doc='glUniform4uiv(GLint(location), GLsizei(count), GLuintArray(value)) -> None',
argNames=('location','count','value',),
deprecated=_DEPRECATED,
)

glTexParameterIiv = platform.createExtensionFunction( 
'glTexParameterIiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glTexParameterIiv(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glTexParameterIuiv = platform.createExtensionFunction( 
'glTexParameterIuiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLuintArray,),
doc='glTexParameterIuiv(GLenum(target), GLenum(pname), GLuintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetTexParameterIiv = platform.createExtensionFunction( 
'glGetTexParameterIiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLintArray,),
doc='glGetTexParameterIiv(GLenum(target), GLenum(pname), GLintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glGetTexParameterIuiv = platform.createExtensionFunction( 
'glGetTexParameterIuiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLenum,arrays.GLuintArray,),
doc='glGetTexParameterIuiv(GLenum(target), GLenum(pname), GLuintArray(params)) -> None',
argNames=('target','pname','params',),
deprecated=_DEPRECATED,
)

glClearBufferiv = platform.createExtensionFunction( 
'glClearBufferiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,arrays.GLintArray,),
doc='glClearBufferiv(GLenum(buffer), GLint(drawbuffer), GLintArray(value)) -> None',
argNames=('buffer','drawbuffer','value',),
deprecated=_DEPRECATED,
)

glClearBufferuiv = platform.createExtensionFunction( 
'glClearBufferuiv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,arrays.GLuintArray,),
doc='glClearBufferuiv(GLenum(buffer), GLint(drawbuffer), GLuintArray(value)) -> None',
argNames=('buffer','drawbuffer','value',),
deprecated=_DEPRECATED,
)

glClearBufferfv = platform.createExtensionFunction( 
'glClearBufferfv',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,arrays.GLfloatArray,),
doc='glClearBufferfv(GLenum(buffer), GLint(drawbuffer), GLfloatArray(value)) -> None',
argNames=('buffer','drawbuffer','value',),
deprecated=_DEPRECATED,
)

glClearBufferfi = platform.createExtensionFunction( 
'glClearBufferfi',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,constants.GLfloat,constants.GLint,),
doc='glClearBufferfi(GLenum(buffer), GLint(drawbuffer), GLfloat(depth), GLint(stencil)) -> None',
argNames=('buffer','drawbuffer','depth','stencil',),
deprecated=_DEPRECATED,
)

glGetStringi = platform.createExtensionFunction( 
'glGetStringi',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=arrays.GLubyteArray, 
argTypes=(constants.GLenum,constants.GLuint,),
doc='glGetStringi(GLenum(name), GLuint(index)) -> arrays.GLubyteArray',
argNames=('name','index',),
deprecated=_DEPRECATED,
)
# import legacy entry points to allow checking for bool(entryPoint)
from OpenGL.raw.GL.VERSION.GL_3_0_DEPRECATED import *