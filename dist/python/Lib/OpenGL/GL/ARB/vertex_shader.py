'''OpenGL extension ARB.vertex_shader

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.vertex_shader to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds programmable vertex level processing to OpenGL. The
	application can write vertex shaders in a high level language as defined
	in the OpenGL Shading Language specification. The language itself is not
	discussed here. A vertex shader replaces the transformation, texture
	coordinate generation and lighting parts of OpenGL, and it also adds
	texture access at the vertex level. Furthermore, management of vertex
	shader objects and loading generic attributes are discussed. A vertex
	shader object, attached to a program object, can be compiled and linked
	to produce an executable that runs on the vertex processor in OpenGL.
	This extension also defines how such an executable interacts with the
	fixed functionality vertex processing of OpenGL 1.4.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/vertex_shader.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.vertex_shader import *
### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy
from shader_objects import glGetObjectParameterivARB

base_glGetActiveAttribARB = glGetActiveAttribARB
def glGetActiveAttribARB(program, index):
    """Retrieve the name, size and type of the uniform of the index in the program"""
    max_index = int(glGetObjectParameterivARB( program, GL_OBJECT_ACTIVE_ATTRIBUTES_ARB ))
    length = int(glGetObjectParameterivARB( program, GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB))
    if index < max_index and index >= 0 and length > 0:
        name = ctypes.create_string_buffer(length)
        size = arrays.GLintArray.zeros( (1,))
        gl_type = arrays.GLuintArray.zeros( (1,))
        base_glGetActiveAttribARB(program, index, length, None, size, gl_type, name)
        return name.value, size[0], gl_type[0]
    raise IndexError, 'index out of range from zero to %i' % (max_index - 1, )
glGetActiveAttribARB.wrappedOperation = base_glGetActiveAttribARB

@lazy( glGetAttribLocationARB )
def glGetAttribLocationARB( baseOperation, program, name ):
    """Check that name is a string with a null byte at the end of it"""
    if not name:
        raise ValueError( """Non-null name required""" )
    elif name[-1] != '\000':
        name = name + '\000'
    return baseOperation( program, name )
