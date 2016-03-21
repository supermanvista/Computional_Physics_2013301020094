a00 = '         '          
a01 = '*        '
a02 = '  *      '
a03 = '* *      '
a04 = '    *    '
a05 = '*   *    '
a06 = '  * *    '
a07 = '* * *    '
a08 = '      *  '
a09 = '*     *  '
a10 = '  *   *  '
a11 = '* *   *  '
a12 = '    * *  '
a13 = '*   * *  '
a14 = '  * * *  '
a15 = '* * * *  '
a16 = '        *'
a17 = '*       *'
a18 = '  *     *'
a19 = '* *     *'
a20 = '    *   *'
a21 = '*   *   *'
a22 = '  * *   *'
a23 = '* * *   *'
a24 = '      * *'
a25 = '*     * *'
a26 = '  *   * *'
a27 = '* *   * *'
a28 = '    * * *'
a29 = '*   * * *'
a30 = '  * * * *'
a31 = '* * * * *'
space = [a00, a00, a00, a00, a00]
A = [a04, a10, a14, a10, a10] 
B = [a14, a10, a06, a10, a14]
C = [a14, a02, a02, a02, a14]
D = [a06, a10, a10, a10, a06]
E = [a14, a02, a14, a02, a14] 
F = [a14, a02, a14, a02, a02]
G = [a15, a01, a29, a09, a15]
H = [a10, a10, a14, a10, a10]
I = [a14, a04, a04, a04, a14]
J = [a14, a04, a04, a05, a07]
K = [a10, a06, a06, a10, a18]
L = [a02, a02, a02, a02, a14]
M = [a10, a10, a21, a21, a21]
N = [a09, a11, a13, a09, a09]
O = [a15, a09, a09, a09, a15]
P = [a14, a10, a14, a02, a02]
Q = [a14, a10, a10, a10, a30]
R = [a14, a18, a14, a10, a18]
S = [a14, a02, a14, a08, a14]
T = [a14, a04, a04, a04, a04]
U = [a10, a10, a10, a10, a14]
V = [a10, a10, a10, a04, a04]
W = [a21, a21, a21, a10, a10]
X = [a10, a10, a04, a10, a10]
Y = [a10, a10, a04, a04, a04]
Z = [a31, a08, a04, a02, a31]
dic = {' ': space, 'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T, 'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}


def drawbeta(a_string):
	def draw(x):
		for i in range(len(x[0])):
			for m in x:
				print m[i],
			print
		print
	def str2var(char):
		return dic[char]
	lst = map(str2var, a_string)
	draw(lst)
drawbeta('C')
drawbeta('DOM')
drawbeta('XIA HAI FENG')
drawbeta('XHF')