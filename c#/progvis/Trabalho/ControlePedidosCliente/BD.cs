using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace ControlePedidosCliente
{
    public class BD
    {
        public static BindingList<Pedido> Pedidos { get; set; }
        public static List<Produto> Produtos { get; set; }

        public BD()
        {
            Pedidos = new BindingList<Pedido>();
            Produtos = new List<Produto>();

            Produto Abacaxi = new Produto
            {
                Codigo = 1,
                Nome = "Abacaxi",
                Preco = 01.10m
            };
            Produto Banana = new Produto
            {
                Codigo = 2,
                Nome = "Banana",
                Preco = 02.20m
            };
            Produto Caqui = new Produto
            {
                Codigo = 3,
                Nome = "Caqui",
                Preco = 03.30m
            };
            Produto Damasco = new Produto
            {
                Codigo = 4,
                Nome = "Damasco",
                Preco = 04.40m
            };
            Produto Faca = new Produto
            {
                Codigo = 5,
                Nome = "Faca PeXERA",
                Preco = 05.50m
            };

            BD.Produtos.Add(Abacaxi);
            BD.Produtos.Add(Banana);
            BD.Produtos.Add(Caqui);
            BD.Produtos.Add(Damasco);
            BD.Produtos.Add(Faca);
        }

        public static List<Produto> ProdutoPerCode(Int64 cod) 
        {
            List<Produto> pds = new List<Produto>();
            foreach (Produto p in Produtos)
            {
                if (p.Codigo == cod)
                {
                    pds.Add(p);
                    break;
                } 
            }

            return pds;

        }
        public static List<Produto> ProdutoPerName(String name)
        {
            List<Produto> pds = new List<Produto>();
            foreach (Produto p in Produtos)
            {
                if (Convert.ToString(p.Nome).Contains(Convert.ToString(name)))
                {
                    pds.Add(p);
                }
            }
            return pds;
        }


    }
}
