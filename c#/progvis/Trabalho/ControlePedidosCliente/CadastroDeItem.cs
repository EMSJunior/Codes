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
    public partial class CadastroDeItem : Form
    {
        private CadastroDeItem()
        {
            InitializeComponent();
        }
        private static CadastroDeItem inst;
        public static CadastroDeItem GetForm()
        {
            if (inst == null || inst.IsDisposed)
                inst = new CadastroDeItem();
            return inst;
        }

        private void txtCod_Click(object sender, EventArgs e)
        {

        }

        private void tableLayoutPanel5_Paint(object sender, PaintEventArgs e)
        {

        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btnSalvar_Click(object sender, EventArgs e)
        {

        }

        private void tbxCod_KeyUp(object sender, KeyEventArgs e)
        {
            if (tbxCod.Text != String.Empty)
            {
                if (System.Text.RegularExpressions.Regex.IsMatch(tbxCod.Text, "[^0-9]"))
                {
                    tbxCod.Text = tbxCod.Text.Remove(tbxCod.Text.Length - 1);
                }
                lbxCdProdutos.DataSource = BD.ProdutoPerCode(Convert.ToInt64(tbxCod.Text));
            }
        }

        private void txbNome_KeyUp(object sender, KeyEventArgs e)
        {
            lbxCdProdutos.DataSource = BD.ProdutoPerName(txtNome.Text);
        }

        private void tbxCod_KeyDown(object sender, KeyEventArgs e)
        {

        }
    }

}
