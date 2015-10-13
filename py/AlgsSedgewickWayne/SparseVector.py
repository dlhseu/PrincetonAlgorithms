#!/usr/bin/env python#*****************************************************************************
 #  Compilation:  javac SparseVector.java
 #  Execution:    java SparseVector
 #  Dependencies: StdOut.java
 #  
 #  A sparse vector, implementing using a symbol table.
 #
 #  [Not clear we need the instance variable N except for error checking.]
 #
 #*****************************************************************************/

package edu.princeton.cs.algs4

#*
 #  The <tt>SparseVector</tt> class represents a <em>d</em>-dimensional mathematical vector.
 #  Vectors are mutable: their values can be changed after they are created.
 #  It includes methods for addition, subtraction,
 #  dot product, scalar product, unit vector, and Euclidean norm.
 #  <p>
 #  The implementation is a symbol table of indices and values for which the vector
 #  coordinates are nonzero. This makes it efficient when most of the vector coordindates
  # are zero.
 #  <p>
 #  For additional documentation,    
 #  see <a href="http://algs4.cs.princeton.edu/35applications">Section 3.5</a> of
 #  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne. 
 #  See also {@link Vector} for an immutable (dense) vector data type.
 #
 #  @author Robert Sedgewick
 #  @author Kevin Wayne
 #/
public class SparseVector:
    private d;                   # dimension
    private ST<Integer, Double> st;  # the vector, represented by index-value pairs

   #*
     # Initializes a d-dimensional zero vector.
     # @param d the dimension of the vector
     #/
    public SparseVector(int d):
        this.d  = d
        this.st = new ST<Integer, Double>()

   #*
     # Sets the ith coordinate of this vector to the specified value.
     #
     # @param  i the index
     # @param  value the new value
     # @throws IndexOutOfBoundsException unless i is between 0 and d-1
     #/
    def put(int i, double value):
        if i < 0 or i >= d) raise new IndexOutOfBoundsException("Illegal index")
        if value == 0.0) st.delete(i)
        else              st.put(i, value)

   #*
     # Returns the ith coordinate of this vector.
     #
     # @param  i the index
     # @return the value of the ith coordinate of this vector
     # @throws IndexOutOfBoundsException unless i is between 0 and d-1
     #/
    def get(int i):
        if i < 0 or i >= d) raise new IndexOutOfBoundsException("Illegal index")
        if st.contains(i)) return st.get(i)
        else:                return 0.0

   #*
     # Returns the number of nonzero entries in this vector.
     #
     # @return the number of nonzero entries in this vector
     #/
    def nnz():
        return st.size()

   #*
     # Returns the dimension of this vector.
     #
     # @return the dimension of this vector
     # @deprecated Replaced by {@link #dimension()}.
     #/
    def size():
        return d

   #*
     # Returns the dimension of this vector.
     #
     # @return the dimension of this vector
     #/
    def dimension():
        return d

    #*
     # Returns the inner product of this vector with the specified vector.
     #
     # @param  that the other vector
     # @return the dot product between this vector and that vector
     # @throws IllegalArgumentException if the lengths of the two vectors are not equal
     #/
    def dot(SparseVector that):
        if this.d != that.d) raise new IllegalArgumentException("Vector lengths disagree")
        double sum = 0.0

        # iterate over the vector with the fewest nonzeros
        if this.st.size() <= that.st.size()):
            for (int i : this.st.keys())
                if that.st.contains(i)) sum += this.get(i) * that.get(i)
        else:
            for (int i : that.st.keys())
                if this.st.contains(i)) sum += this.get(i) * that.get(i)
        return sum


    #*
     # Returns the inner product of this vector with the specified array.
     #
     # @param  that the array
     # @return the dot product between this vector and that array
     # @throws IllegalArgumentException if the dimensions of the vector and the array are not equal
     #/
    def dot(double[] that):
        double sum = 0.0
        for (int i : st.keys())
            sum += that[i] * this.get(i)
        return sum

    #*
     # Returns the magnitude of this vector.
     # This is also known as the L2 norm or the Euclidean norm.
     # 
     # @return the magnitude of this vector
     #/
    def magnitude():
        return Math.sqrt(this.dot(this))


    #*
     # Returns the Euclidean norm of this vector.
     #
     # @return the Euclidean norm of this vector
     # @deprecated Replaced by {@link #magnitude()}.
     #/
    def norm():
        return Math.sqrt(this.dot(this))

    #*
     # Returns the scalar-vector product of this vector with the specified scalar.
     #
     # @param  alpha the scalar
     # @return the scalar-vector product of this vector with the specified scalar
     #/
    def scale(double alpha):
        SparseVector c = new SparseVector(d)
        for (int i : this.st.keys()) c.put(i, alpha * this.get(i))
        return c

    #*
     # Returns the sum of this vector and the specified vector.
     #
     # @param  that the vector to add to this vector
     # @return the sum of this vector and that vector
     # @throws IllegalArgumentException if the dimensions of the two vectors are not equal
     #/
    def plus(SparseVector that):
        if this.d != that.d) raise new IllegalArgumentException("Vector lengths disagree")
        SparseVector c = new SparseVector(d)
        for (int i : this.st.keys()) c.put(i, this.get(i));                # c = this
        for (int i : that.st.keys()) c.put(i, that.get(i) + c.get(i));     # c = c + that
        return c

   #*
     # Returns a string representation of this vector.
     # @return a string representation of this vector, which consists of the 
     #         the vector entries, separates by commas, enclosed in parentheses
     #/
    def toString():
        StringBuilder s = new StringBuilder()
        for (int i : st.keys()):
            s.append("(" + i + ", " + st.get(i) + ") ")
        return s.toString()


    #*
     # Unit tests the <tt>SparseVector</tt> data type.
     #/
    def main(String[] args):
        SparseVector a = new SparseVector(10)
        SparseVector b = new SparseVector(10)
        a.put(3, 0.50)
        a.put(9, 0.75)
        a.put(6, 0.11)
        a.put(6, 0.00)
        b.put(3, 0.60)
        b.put(4, 0.90)
        prt.write("a = " + a)
        prt.write("b = " + b)
        prt.write("a dot b = " + a.dot(b))
        prt.write("a + b   = " + a.plus(b))


#*****************************************************************************
 #  Copyright 2002-2015, Robert Sedgewick and Kevin Wayne.
 #
 #  This file is part of algs4.jar, which accompanies the textbook
 #
 #      Algorithms, 4th edition by Robert Sedgewick and Kevin Wayne,
 #      Addison-Wesley Professional, 2011, ISBN 0-321-57351-X.
 #      http://algs4.cs.princeton.edu
 #
 #
 #  algs4.jar is free software: you can redistribute it and/or modify
 #  it under the terms of the GNU General Public License as published by
 #  the Free Software Foundation, either version 3 of the License, or
 #  (at your option) any later version.
 #
 #  algs4.jar is distributed in the hope that it will be useful,
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with algs4.jar.  If not, see http://www.gnu.org/licenses.
 #*****************************************************************************/
