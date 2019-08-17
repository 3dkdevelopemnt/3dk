'''OpenGL extension EXT.geometry_shader4

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_geometry_shader4'
_DEPRECATED = False
GL_GEOMETRY_SHADER_EXT = constant.Constant( 'GL_GEOMETRY_SHADER_EXT', 0x8DD9 )
GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT = constant.Constant( 'GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT', 0x8DDD )
glget.addGLGetConstant( GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT, (1,) )
GL_MAX_VERTEX_VARYING_COMPONENTS_EXT = constant.Constant( 'GL_MAX_VERTEX_VARYING_COMPONENTS_EXT', 0x8DDE )
glget.addGLGetConstant( GL_MAX_VERTEX_VARYING_COMPONENTS_EXT, (1,) )
GL_MAX_VARYING_COMPONENTS_EXT = constant.Constant( 'GL_MAX_VARYING_COMPONENTS_EXT', 0x8B4B )
glget.addGLGetConstant( GL_MAX_VARYING_COMPONENTS_EXT, (1,) )
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT = constant.Constant( 'GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT', 0x8DDF )
glget.addGLGetConstant( GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT, (1,) )
GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT = constant.Constant( 'GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT', 0x8DE0 )
glget.addGLGetConstant( GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT, (1,) )
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT = constant.Constant( 'GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT', 0x8DE1 )
glget.addGLGetConstant( GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT, (1,) )
glProgramParameteriEXT = platform.createExtensionFunction( 
'glProgramParameteriEXT',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLuint,constants.GLenum,constants.GLint,),
doc='glProgramParameteriEXT(GLuint(program), GLenum(pname), GLint(value)) -> None',
argNames=('program','pname','value',),
deprecated=_DEPRECATED,
)


def glInitGeometryShader4EXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )