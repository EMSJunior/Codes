using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ComponentModel;

namespace Gestão_de_Compras
{
    public class BancoDeDados
    {
        public static BindingList<Produto> Produtos { get; set; }
        public static BindingList<Compra> Compras { get; set; }

        static BancoDeDados()
        {
            Produtos = new BindingList<Produto>();
            Compras = new BindingList<Compra>();

            Produtos.Add(new Produto(0, "A", 00.00m));
            Produtos.Add(new Produto(1, "B", 00.00m));
            Produtos.Add(new Produto(2, "C", 00.00m));
            Produtos.Add(new Produto(3, "D", 00.00m));
            Produtos.Add(new Produto(4, "E", 00.00m));
            Produtos.Add(new Produto(5, "F", 00.00m));
            Produtos.Add(new Produto(6, "G", 00.00m));
            Produtos.Add(new Produto(7, "H", 00.00m));
            Produtos.Add(new Produto(8, "I", 00.00m));
            Produtos.Add(new Produto(9, "J", 00.00m));
            Produtos.Add(new Produto(10, "K", 00.00m));
            Produtos.Add(new Produto(11, "L", 00.00m));
            Produtos.Add(new Produto(12, "M", 00.00m));
            Produtos.Add(new Produto(13, "N", 00.00m));


        }

        public static List<Produto> Buscar(String parte)
        {
            List<Produto> produtos = new List<Produto>();
            try
            {
                Convert.ToInt64(parte);
                foreach (Produto produto in Produtos)
                {
                    if (produto.Nome.ToLower().Contains(parte.ToLower()))
                    {
                        produtos.Add(produto);
                    }
                    if (produto.Codigo == Convert.ToInt64(parte))
                    {
                        produtos.Add(produto);
                    }
                }
            }
            catch
            {

                foreach (Produto produto in Produtos)
                {
                    if (produto.Nome.ToLower().Contains(parte.ToLower()))
                    {
                        produtos.Add(produto);
                    }
                    
                }
            }

            return produtos;
        }

        public static bool VerificarLote(Int64 l)
        {
            foreach(var lote in Compras)
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
