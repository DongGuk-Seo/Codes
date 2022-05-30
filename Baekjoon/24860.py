# 문제
# Immunoglobulins also known as antibodies are protein molecules. Antibodies play one of the key roles in the immune reaction --- they detect harmful foreign agents --- bacteria or viruses --- and help to eliminate them. Every foreign molecule binds with unique type of antibody. There are plenty of potential harmful agents, so, there should be a tremendous number of immunoglobulin types to neutralize all threats. Huge required amount of immunoglobulin types make it impossible to encode each type in DNA. Luckily, there is a solution.

# Immunoglobulins are produced by immune cells: B-lymphocytes based on DNA information --- genes. Immunoglobulin genes are combined from DNA fragments like constructor. Each fragment exists in several variants and is responsible for variable region of immunoglobulin molecule. This process is called somatic recombination. 

# Immunoglobulin molecule consists of two identical heavy chains and two identical light chains. There are two types of light chains with similar structure --- $\kappa$ and $\lambda$. Both of two light chain types have two variable regions --- $V$ and $J$. To form a variable region one gene fragment is selected from multiple variants: $V_\kappa$ and $J_\kappa$ variants for $V$ and $J$ regions respectively in $\kappa$-light chain, or $V_\lambda$ and $J_\lambda$ variants for $V$ and $J$ regions respectively in $\lambda$-light chain.

# There is only one heavy chain type with three variable regions --- $V$, $D$ and $J$. To form each of them one gene fragment from $V_h$, $D_h$ and $J_h$ variants respectively is selected.



# You need to count how many possible immunoglobulin molecules can be produced for given values of $V_\kappa$, $J_\kappa$, $V_\lambda$, $J_\lambda$, $V_h$, $D_h$ and $J_h$.

# 입력
# The first line contains two integers $V_\kappa$, $J_\kappa$ ($1 \leq V\kappa, J\kappa \leq 1500$) --- number of gene fragment variants for $\kappa$-light chain  $V$ and $J$ variable regions, respectively.

# The second line contains two integers $V_\lambda$, $J_\lambda$ ($1 \leq V_\lambda, J_\lambda \leq 1500$) --- number of gene fragment variants for $\lambda$-light chain $V$ and $J$ variable regions, respectively.

# The third line contains three integers $V_h$, $D_h$ and $J_h$ ($1 \leq V_h, D_h, J_h \leq 1000$) --- number of gene fragment variants for heavy chain $V$, $D$ and $J$ variable regions, respectively.

# 출력
# Output one integer --- number of immunoglobulin variants that can be produced.

vk, jk = map(int,input().split())
vl, jl = map(int,input().split())
vh, dh, jh  = map(int,input().split())
print((vh*dh*jh*vk*jk)+(vh*dh*jh*vl*jl))