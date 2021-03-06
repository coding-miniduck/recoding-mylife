import os
import json


with open('struct.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)

doc_text='''
    <!DOCTYPE html>
    <html lang="kor">
    <head>
        <meta charset="UTF-8">
        
        <title>Document</title>
        
        <script type="text/x-mathjax-config">
            MathJax.Hub.Config({            
                tex2jax: {inlineMath: [['$','$']]},
                CommonHTML: {
                    scale: 65
                }     
            });
        </script>
        <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML' async></script>
        
        <link href='a4_style.css' rel='stylesheet' type='text/css'>

    </head>
    <body>
        <div class="book">
            <div class="page">
                <div class="phead">
                    <table>
                        <tr>
                            <td id=ptitle>테일러 급수 </td>
                            <td>
                                <table id=info>
                                    <tr>
                                        <td>doc_id</td>
                                        <td>123020</td>
                                    </tr>
                                    <tr>
                                        <td>date</td>
                                        <td>2021-10-20</td>
                                    </tr>
                                    <tr>
                                        <td>author</td>
                                        <td>2630 정승민</td>
                                    </tr>
                                    <tr>
                                        <td>note</td>
                                        <td>example</td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </div>
                <div class="ptable">
                    <table>
                        <tr>
                            <td>1. 정의<sup><a id="up_ref[1]" href="#down_ref[1]">[1]</a></sup></td>
                            <td>(중심 <span id=math_0>$x_0$</span>의 멱급수) <span id=math_1>$ = \displaystyle\sum_{n=0}^{\infty} a_n(x-x_0)^{n}$</span>  <span id=math_2>$(x_0, a_0, a_1, a_2, \cdots \in $</span> <span id=math_3>$\mathbb{K}$</span>, <span id=math_4>$\mathbb{K}$</span> 는 <span id=math_5>$\mathbb{R}$</span> 혹은 <span id=math_6>$\mathbb{C})$</span><sup><a id="up_ref[2]" href="#down_ref[2]">[2]</a></sup> <br>
                                매끄러운 함수 $f \Leftrightarrow f$는 무한법 미분가능하다. <br>
                                매끄러운 함수 $f: \mathbb{R} \\rightarrow \mathbb{R}$, $a \in \mathbb{R}$가 주어질때 <br>
                                $f$의 테일러 급수는 다음과 같은 멱급수 <br>
                                $T_{f(x)} = \displaystyle\sum_{n=0}^{\infty} \\frac{f^{(n)}(a)}{n!} = f(a) + f^{\prime}(a)(x-a) + \\frac{1}{2}f^{\prime\prime}(a)(x-a)^2 + \cdots$ <sup><a id="up_ref[3]" href="#down_ref[3]">[3]</a></sup> <br>
                                특히 $(a=0)$일 때의 테일러 급수를 매클로린 급수라 부른다.
                            </td>
                        </tr>
                        <tr>
                            <td>2. 대표 예<sup><a id="up_ref[1]" href="#down_ref[1]">[1]</a></sup></td>
                            <td>$\\frac{1}{1-x} = \displaystyle \sum_{n=0}^{\infty} \\frac{f^{(n)}(x)}{n!}(x-a)^{n} = 1+x+x^2+x^3+ \cdots $ &nbsp;&nbsp;&nbsp; $e^x = \displaystyle\sum_{n=0}^{\infty} \\frac{x^n}{n!} = 1+x+\\frac{1}{2!}x^2+\\frac{1}{3!}x^3+\\frac{1}{4!}x^4+\cdots$ <br>
                                $\sin x = \displaystyle\sum_{n=0}^{\infty} \\frac{(-1)^n}{(2n+1)!}x^{2n+1} = x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\cdots $ &nbsp;&nbsp;&nbsp; $\cos x = \displaystyle\sum_{n=0}^{\infty} \\frac{(-1)^n}{2n!}x^{2n} = 1-\\frac{x^2}{2!}+\\frac{x^4}{4!}-\cdots$ <br>
                                $\ln (1-x) = \displaystyle\sum_{n=1}^{\infty} \\frac{x^n}{n} = -x-\\frac{1}{2}x^2-\\frac{1}{3}x^3- \cdots $ &nbsp;&nbsp;&nbsp; $\ln (1+x) = \displaystyle\sum_{n=1}^{\infty} \\frac{(-1)^{n-1}}{n}x^n = x-\\frac{x^2}{2}+\\frac{x^3}{3}-\\frac{x^4}{4}+\cdots $
                            </td>
                        </tr>
                        <tr>
                            <td>3. 유용성</td>
                            <td>
                                <ul>
                                    <li>근사값 구하기가 가능해짐 ex) $\sin (1) = 1-\\frac{1}{3!}+\\frac{1}{3!}-\cdots \, \\fallingdotseq \,0.841 \dots$</li>
                                    <li>분석에 용이함</li>
                                    <ul>
                                        <li>$\sin x$는 모든 항의 차수가 홀수 $\Leftrightarrow$ 기함수, 마찬가지로 $\cos x$는 우함수인 점</li>
                                        <li>$-\ln (1-x)$에서 각 항을 미분하면 $\\frac{1}{1-x}$와 같은 꼴 $\Leftrightarrow (-\ln (1-x))^{\prime} = \\frac{1}{1-x}$</li>
                                        <li>$\displaystyle\lim_{x \\rightarrow 0} \\frac{\sin x}{x} = \lim_{x \\rightarrow 0} \\frac{x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\cdots}{x} = 1$</li>
                                    </ul>
                                </ul>
                            </td>
                        </tr>
                    </table>
                </div>
                <div class="pref">
                    <table>
                        <tr>
                            <td>[ ] 각주</td>
                            <td><ul>
                                <li id="down_ref[1]"><a href="#up_ref[1]">[1]</a> 위키백과 '테일러 급수', '매끄러운 함수', '멱급수' 문서에서 가져옴</li>
                                <li id="down_ref[2]"><a href="#up_ref[2]">[2]</a> R는 실수체, C는 복소수체</li>
                                <li id="down_ref[3]"><a href="#up_ref[3]">[3]</a> f(n)(x)는 f(x)의 n계도 함수</li>
                            </ul></td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
        
    </body>
    </html>
'''

path=os.getcwd()+'\\test\\test.html'
print(path)
with open(path, 'w', encoding='utf-8') as f:
    f.write(doc_text)