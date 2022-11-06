using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Gestão_de_Compras
{
    public class Compras
    {
    public Int64 Lote { get; set; }    
    public DateTime Compra { get; set; }
    public DateTime Vencimento { get; set; }
    public Int16 Quantidade { get; set; }
    public Produto Produto { get; set; }

    public Decimal Total
    {
        get
        {
            return CalcularTotal();
        }
    }


        public  Decimal CalcularTotal()
        {
            return Quantidade * Produto.Preco ;
        }
    }

}
