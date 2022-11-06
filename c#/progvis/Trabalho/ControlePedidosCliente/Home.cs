using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ControlePedidosCliente
{
    public partial class Home : Form
    {
        public BD bd { get; set; } = new BD();
   
        public Home()
        {
            InitializeComponent();
            IsMdiContainer = true;
        }

        private void Home_Load(object sender, EventArgs e)
        {

        }

        private void tsmSair_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void tmsPedido_Click(object sender, EventArgs e)
        {
            var j = Pedidos.GetForm();
            if (j.MdiParent == null)
            {
                j.MdiParent = this;
                j.Show();
            } else
            {
                j.WindowState = FormWindowState.Normal;
            }
            j.Activate();

        }

        private void tsmProdutos_Click(object sender, EventArgs e)
        {
            var j = Produtos.GetForm();
            if (j.MdiParent == null)
            {
                j.MdiParent = this;
                j.Show();
            }
            else
            {
                j.WindowState = FormWindowState.Normal;
            }
            j.Activate();

        }
    }
}
