using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ControlePedidosCliente
{
    public class Produto
    {
        public Int64 Codigo { get; set; }
        public string Nome { get; set; }
        public Decimal Preco { get; set; }

        public override string ToString()
        {
            return $"{Nome}   >||R${Preco}||";
        }

    }
}
