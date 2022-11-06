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
            Produto a = new Produto(0, "Alavanca", 149.90m);
            Produtos.Add(a);
            Produtos.Add(new Produto(1, "Bicicleta", 1199.30m));
            Produto b = new Produto(2, "C#", 300.00m);
            Produtos.Add(b);
            Produtos.Add(new Produto(3, "Dinheiro LIMPO", 01.00m));
            Produtos.Add(new Produto(4, "Elon Musk", 1_500_000_000.00m));
            Produto c = new Produto(5, "Free Fire", 10.00m);
            Produtos.Add(c);
            Produtos.Add(new Produto(6, "Gato de energia", 400.00m));
            Produtos.Add(new Produto(7, "Hitler", 19.45m));
            Produtos.Add(new Produto(8, "Instituto Federal", 00.01m));
            Produtos.Add(new Produto(9, "Jaca", 01.50m));
            Produto d = new Produto(10, "KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK", 656.00m);
            Produtos.Add(d);
            Produtos.Add(new Produto(11, "Lula", 00.00m));
            Produtos.Add(new Produto(12, "Doze n é um numero muito sugestivo", 12.00m));
            Produtos.Add(new Produto(14, "Ovo podi", 54.00m));
            Produtos.Add(new Produto(15, "Principe encantado", 47568.48m));
            Produtos.Add(new Produto(16, "Query", 99.99m));
            Produtos.Add(new Produto(17, "Ran dan dan dan", 127.99m));
            Produtos.Add(new Produto(18, "Saturno", 100_000_000_000.00m));
            Produtos.Add(new Produto(19, "Telefone de Jesus", 800_000.00m));
            Produtos.Add(new Produto(20, "Utero", 60000.00m));
            Produtos.Add(new Produto(21, "Vaca leiteira 15l/dia", 1_300_000.00m));
            Produtos.Add(new Produto(22, "Wolsonaro", 22.22m));

            Compras.Add(new Compra
            {
                DataCompra = DateTime.Today.Date,
                Vencimento = DateTime.Today.Date,
                Lote = 0,
                Produto = a,
                Quantidade = 0
            });
            Compras.Add(new Compra
            {
                DataCompra = DateTime.Today.Date,
                Vencimento = DateTime.Today.Date.AddDays(1),
                Lote = 1,
                Produto = b,
                Quantidade = 1
            });
            Compras.Add(new Compra
            {
                DataCompra = DateTime.Today.Date,
                Vencimento = DateTime.Today.Date.AddDays(5),
                Lote = 5,
                Produto = c,
                Quantidade = 5
            });
            Compras.Add(new Compra
            {
                DataCompra = DateTime.Today.Date,
                Vencimento = DateTime.Today.Date.AddDays(10),
                Lote = 10,
                Produto = d,
                Quantidade = 10
            });

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
                        continue;
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

        public static Compra VerificarLote(Int64 l)
        {
            foreach (var lote in Compras)
            {
                if (lote.Lote == l)
                {
                    return lote;
                }
            }
            return null;
        }
    }
}
