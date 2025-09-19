<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>README — Resolução de Sistemas Lineares (Gauss, LU, Jacobi, Gauss–Seidel)</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --accent:#6ee7b7; --muted:#94a3b8;
      --glass: rgba(255,255,255,0.04);
      --mono: 'Courier New', monospace;
    }
    *{box-sizing:border-box}
    body{margin:0;font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; background:linear-gradient(180deg,#071023 0%, #081227 60%); color:#e6eef6; line-height:1.5}
    .wrap{max-width:980px;margin:48px auto;padding:28px}
    header{display:flex;gap:20px;align-items:center}
    .logo{width:76px;height:76px;border-radius:12px;background:linear-gradient(135deg,var(--accent),#60a5fa);display:flex;align-items:center;justify-content:center;box-shadow:0 8px 30px rgba(6,8,20,.6);font-weight:700;color:#022;}
    h1{margin:0;font-size:22px}
    p.lead{color:var(--muted);margin-top:6px}

    .grid{display:grid;grid-template-columns:1fr 320px;gap:22px;margin-top:26px}
    .card{background:linear-gradient(180deg,var(--card), rgba(11,18,32,0.6));border-radius:12px;padding:18px;box-shadow:0 10px 30px rgba(2,6,23,.6);}

    .section-title{font-size:14px;color:var(--accent);letter-spacing:0.06em;margin-bottom:10px}

    .kpi{display:flex;gap:10px;flex-wrap:wrap}
    .pill{background:var(--glass);padding:8px 12px;border-radius:999px;color:var(--muted);font-size:13px}

    pre{background:#071229;padding:14px;border-radius:8px;overflow:auto;font-family:var(--mono);font-size:13px}

    .methods{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
    .method{background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent);padding:12px;border-radius:10px}
    .method h4{margin:0 0 6px 0;color:var(--accent)}
    .math{background:rgba(255,255,255,0.02);padding:12px;border-radius:8px;color:#dbeafe;font-family:serif}

    footer{margin-top:20px;color:var(--muted);font-size:13px;display:flex;justify-content:space-between;align-items:center}

    /* Copy button */
    .copy-row{display:flex;justify-content:flex-end}
    .btn{background:transparent;border:1px solid rgba(255,255,255,0.06);padding:8px 10px;border-radius:8px;color:var(--accent);cursor:pointer;font-weight:600}
    .btn.small{padding:6px 8px;font-size:13px}

    /* Responsive */
    @media (max-width:900px){.grid{grid-template-columns:1fr}.methods{grid-template-columns:1fr}}
  </style>
  <script>
    // Copy code helper
    function copyCode(id){
      const t = document.getElementById(id).innerText;
      navigator.clipboard.writeText(t).then(()=>{
        const btn = event.currentTarget || document.querySelector('#btn-'+id);
        btn.innerText = 'Copiado!';
        setTimeout(()=> btn.innerText = 'Copiar', 1200);
      });
    }
  </script>
  <!-- MathJax for nice maths -->
  <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">MD</div>
      <div>
        <h1>Resolução de Sistemas Lineares — Gauss, LU, Jacobi e Gauss–Seidel</h1>
        <p class="lead">Exemplo didático e comentado em Python. Implementações orientadas ao estudante — com passos e comentários para aprendizado.</p>
      </div>
    </header>

    <div class="grid">
      <main class="card">
        <div class="section-title">Visão Geral</div>
        <p>Este repositório contém implementações em Python para resolver sistemas lineares \(A x = b\) usando métodos diretos e iterativos. O objetivo é didático: código legível, comentários explicativos e comparação entre técnicas.</p>

        <div style="margin-top:14px" class="kpi">
          <span class="pill">Direto: Gauss, LU</span>
          <span class="pill">Iterativo: Jacobi, Gauss–Seidel</span>
          <span class="pill">Formato: .py (fácil de ler)</span>
        </div>

        <hr style="margin:18px 0;border:none;border-top:1px dashed rgba(255,255,255,0.04)">

        <div class="section-title">Matemática (resumo)</div>
        <div class="math">
          <p><strong>Problema:</strong> resolver \(A x = b\), onde \(A\in\mathbb{R}^{n\times n}\) e \(b\in\mathbb{R}^n\).</p>

          <p><strong>Eliminação de Gauss:</strong> transformar \(A\) em forma triangular superior \(U\) através de operações elementares; em seguida, resolver \(U x = \tilde b\) por retrossubstituição.</p>

          <p><strong>Fatoração LU:</strong> encontrar \(L\) (triangular inferior com diagonal unitária) e \(U\) (triangular superior) tal que \(A = L U\). Resolve-se \(L y = b\) por substituição direta e depois \(U x = y\) por retrossubstituição.</p>

          <p><strong>Jacobi:</strong> método iterativo que usa a decomposição \(A = D + R\) (onde \(D\) é diagonal). Iteração:
          \[ x^{(k+1)} = D^{-1}\left(b - R x^{(k)}\right). \]</p>

          <p><strong>Gauss–Seidel:</strong> versão sequencial de Jacobi que atualiza componentes de \(x\) imediatamente:
          \[ x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j< i} a_{ij} x_j^{(k+1)} - \sum_{j> i} a_{ij} x_j^{(k)}\right).\]</p>
        </div>

        <hr style="margin:18px 0;border:none;border-top:1px dashed rgba(255,255,255,0.04)">

        <div class="section-title">Complexidade e observações</div>
        <ul style="color:var(--muted);margin-top:8px">
          <li><strong>Gauss / LU:</strong> custo assintótico de \(O(n^3)\) para fatoração; solução de subsistemas \(O(n^2)\).</li>
          <li><strong>Jacobi / Gauss–Seidel:</strong> custo por iteração \(O(n^2)\); convergência depende de propriedades da matriz (ex.: diagonal dominante).</li>
          <li>Para sistemas grandes e esparsos, prefira métodos iterativos e bibliotecas especializadas (SciPy, PETSc).</li>
        </ul>

        <hr style="margin:18px 0;border:none;border-top:1px dashed rgba(255,255,255,0.04)">

        <div class="section-title">Uso</div>
        <p style="color:var(--muted)">Copie o arquivo Python para o seu repositório, execute com Python 3.8+ e experimente alterar a matriz de exemplo. As funções retornam vetores solução e matrizes (quando aplicável).</p>

        <div style="margin-top:12px">
          <div style="display:flex;align-items:center;justify-content:space-between">
            <strong>Trecho principal (exemplo de execução)</strong>
            <button class="btn small" id="btn-code-main" onclick="copyCode('code-main')">Copiar</button>
          </div>
          <pre id="code-main"># Exemplo de uso (Python)
a = [[5,2,1],[-1,4,2],[2,-3,10]]
b = [-12,20,3]
L,U,x = lu(a,b)
print('L=',L)  # matriz L
print('U=',U)  # matriz U
print('x=',x)  # solução</pre>
        </div>

      </main>

      <aside class="card">
        <div class="section-title">Conteúdo do README</div>
        <ol style="color:var(--muted);margin:8px 0;padding-left:16px">
          <li>Introdução</li>
          <li>Matemática</li>
          <li>Complexidade</li>
          <li>Implementação (resumo)</li>
          <li>Exemplo</li>
          <li>Licença</li>
        </ol>

        <div style="margin-top:10px">
          <div class="section-title">Blocos de código</div>
          <div class="methods">
            <div class="method">
              <h4>Gauss / LU</h4>
              <pre id="code-lu">def lu(a,b):\n  # ... implementação ...</pre>
              <div class="copy-row"><button class="btn" id="btn-code-lu" onclick="copyCode('code-lu')">Copiar</button></div>
            </div>
            <div class="method">
              <h4>Iterativos</h4>
              <pre id="code-iter">def jacobi(...):\n  # ...\ndef gauss_seidel(...):\n  # ...</pre>
              <div class="copy-row"><button class="btn" id="btn-code-iter" onclick="copyCode('code-iter')">Copiar</button></div>
            </div>
          </div>
        </div>

        <div style="margin-top:16px">
          <div class="section-title">Licença</div>
          <p style="color:var(--muted)">MIT — sinta-se livre para copiar, modificar e citar. Mantenha referência ao autor quando for distribuído.</p>
        </div>

      </aside>
    </div>

    <footer>
      <div>&copy; Maria Eduarda — Implementações docentes</div>
      <div style="color:var(--muted)">Sugestão: incluir testes e notebooks para visualização</div>
    </footer>
  </div>
</body>
</html>
