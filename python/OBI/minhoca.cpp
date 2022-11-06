#include <cstdio>
#include <vector>

constexpr int maxn = 1e5+10;

std::vector<int> g[maxn];

struct Par {
	int tam, qtd;
	bool operator>(const Par& o) const { return tam > o.tam; }
	bool operator==(const Par& o) { return tam == o.tam; }
};

int cnt[maxn]; // ao invés de salvar a resposta máxima vou salvar quantos ativos existem de cada caminho máximo e so checo no final

Par dfs(int u, int p) {
	// coleto todos os valores de dist dos filhos em um vetor
	std::vector<Par> aq = {{0, 1}}; // esse valor de distância 0 que existe para todos é simplesmente o próprio vértice
	for(int v : g[u]) if(v != p)
		aq.push_back(dfs(v, u));

	// encontrando os filhos com maiores distâncias
	int ff = 0, ss = 0;
	for(int i = 0; i < (int)(aq.size()); i++)
		if(aq[i] > aq[ff]) ss = ff, ff = i;
		else if(aq[i] > aq[ss]) ss = i;

	std::vector<Par> aux;

	for(int i = 0; i < (int)(aq.size()); i++)
		if(aq[i] == aq[ss]) aux.push_back(aq[i]);

	// caso [1], existem vários maiores valores e queremos parear todos eles 1 a 1
	if(aq[ff] == aq[ss]) {
		int foi = 0, ans = 0;
		for(int i = 0; i < (int)(aux.size()); i++)
			ans += foi * aux[i].qtd, foi += aux[i].qtd;

		cnt[2*aq[ff].tam + 1] += ans;
		
		return {aq[ff].tam + 1, foi};
	}

	// aq[ff] > aq[ss], caso [2], existe somente 1 maior porém podem existir vários segundos maiores (ou somente 1)
	int ans = 0;
	for(int i = 0; i < (int)(aux.size()); i++)
		ans += aq[ff].qtd * aux[i].qtd;

	cnt[aq[ff].tam + aq[ss].tam + 1] += ans;

	return {aq[ff].tam + 1, aq[ff].qtd};
}

int main() {
	int n; scanf("%d", &n);
	for(int i = 1, a, b; i < n; i++)
		scanf("%d %d", &a, &b), g[a].push_back(b), g[b].push_back(a);

	dfs(1, 0);

	for(int i = maxn-1; i >= 0; i--)
		if(cnt[i]) return printf("%d\n%d\n", i, cnt[i]), 0;
}