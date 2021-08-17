import numpy
cimport numpy
from CyOpenGL cimport (
    # GL_FALSE,
    # GL_TEXTURE0,
    # GL_TEXTURE_2D,
    GLuint,
    GLint,
    GLfloat,
    GLsizei,
    GLenum,
    glUseProgram,
    glUniformMatrix4fv,
    glUniform1i,
    glBindVertexArray,
    glActiveTexture,
    glBindTexture,
    glDrawArrays,
)

cpdef draw(self, transformation_matrix: numpy.ndarray):
    cdef GLfloat[:] transform = transformation_matrix.T.astype(numpy.float32).ravel()
    cdef GLenum mode = self.draw_mode
    cdef GLint first = self.draw_start
    cdef GLsizei count = self.draw_count
    cdef GLuint shader = self._shader
    cdef GLint transform_location = self._transform_location
    cdef GLint texture_location = self._texture_location
    cdef GLuint texture = self._texture
    cdef GLuint vao = self._vao

    glUseProgram(shader)
    glUniformMatrix4fv(
        transform_location,
        1,
        0,
        transform,
    )
    glUniform1i(texture_location, 0)
    glBindVertexArray(vao)
    glActiveTexture(0x84C0)
    glBindTexture(0x0DE1, texture)
    glDrawArrays(mode, first, count)
    glBindVertexArray(0)
    glUseProgram(0)
