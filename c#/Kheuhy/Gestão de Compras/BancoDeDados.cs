using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;
namespace Gestão_de_Compras
{
    public  class BancoDeDados
    {
    public static BindingList<Produto> Produtos { get; set; }
    public static BindingList<Compras> Compras{ get; set; }

    static BancoDeDados()
        {
            Produtos = new BindingList<Produto>();
            Compras = new BindingList<Compras>();

            Produtos.Add(new Produto(1, "leite", 8.95m));
            Produtos.Add(new Produto(2, "Arroz", 18.90m));
            Produtos.Add(new Produto(1, "Grão de Bico",30.00m));
            Produtos.Add(new Produto(1, "Iogurte ", 25.00m));
            Produtos.Add(new Produto(1, "Batta Palha", 35.95m));
            Produtos.Add(new Produto(1, "Requeijão", 22.00m));
            Produtos.Add(new Produto(1, "Margarina", 10.95m));
            Produtos.Add(new Produto(1, "Pão integral", 15.95m));
        }

        public static List<Produto> Busca(String parte)
        {
            List<Produto> produtos = new List<Produto>();

            foreach (Produto produto in Produtos)
            {
                if (produto.Nome.ToLower().Contains(parte.ToLower()))
                {
                    produtos.Add(produto);
                }
                try
                {
                    if (Convert.ToInt64(parte) == produto.Codigo)
                    {
                        produtos.Add(produto);
                    }
                } catch { }
            }
            return produtos;
        }
        public static bool VerificarLote(Int64 l)
        {
            foreach (var lote in Compras)
            {
                if (lote.Lote == l)
                {
                    return true;
                }
            }
            return false;
        }
    }
}
