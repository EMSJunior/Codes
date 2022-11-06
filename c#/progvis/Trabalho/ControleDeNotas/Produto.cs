using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Gestão_de_Compras
{
    public class Produto
    {
        public Int64 Codigo { get; set; }

        public String Nome { get; set; }

        public Decimal Preco { get; set; }

        public Produto(Int64 c, String n, Decimal p)
        {
            Codigo = c;
            Nome = n;
            Preco = p;
        }
        public Produto()
        {

        }
        public override string ToString()
        {
            return Codigo + " - " + Nome + " > R$ " + Preco;
        }
    }
}
