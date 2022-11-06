using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Gestão_de_Compras
{
    public partial class NovoLote : Form
    {
        private NovoLote()
        {
            InitializeComponent();
        }
        public static Compra compra;
        static NovoLote()
        {
            compra = new Compra();
        }

        private static NovoLote instance { get; set; }
        public static NovoLote GetInstance()
        {

            if (instance == null || instance.IsDisposed)
            {
                instance = new NovoLote();
            }
            return instance;
        }

        private void NovoLote_Load(object sender, EventArgs e)
        {

        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btnSalvar_Click(object sender, EventArgs e)
        {
            // MEXER NOS NOMES DOS ALERTAS

            try
            {                
                if (BancoDeDados.VerificarLote(Convert.ToInt64(txtLote.Text)))
                {
                    MessageBox.Show("Este Lote já existe", "Erro");
                    txtLote.Text = "";
                    return;
                    
                }
            }
            catch
            {
                MessageBox.Show("Lote", "Erro");
                return;
            }

            try
            {
                compra.Lote = Convert.ToInt64(txtLote.Text);
            }
            catch
            {
                MessageBox.Show("lote", "Erro");
                return;
            }

            try
            {
                compra.DataCompra = dtpCompra.Value;
                compra.Vencimento = dtpVencimento.Value;
            }
            catch
            {
                MessageBox.Show("data", "Erro");
                return;
            }

            try
            {
                compra.Quantidade = Convert.ToInt16(nudQuantidade.Value);
            }
            catch
            {
                MessageBox.Show("quantidade", "Erro");
                return;
            }

            if (lstLote.SelectedItem == null)
            {
                MessageBox.Show("nenhum produto", "Erro");
                return;
            }
            else
            {
                compra.Produto = (Produto)lstLote.SelectedItem;
            }

            BancoDeDados.Compras.Add(compra);
            compra = new Compra();

            txtProduto.Text = "";
            txtLote.Text = "";
            dtpCompra.Value = DateTime.Now;
            dtpVencimento.Value = DateTime.Now.AddDays(1);
            nudQuantidade.Value = 1;
            lblTotal.Text = "Total: R$";
            lstLote.DataSource = null;

        }

        private void txtProduto_TextChanged(object sender, EventArgs e)
        {
            if (txtProduto.Text == "")
            {
                return;
            }
            lstLote.DataSource = BancoDeDados.Buscar(txtProduto.Text);
            CalcularTotal();
        }

        private void nudQuantidade_ValueChanged(object sender, EventArgs e)
        {
            CalcularTotal();
        }

        private void lstLote_SelectedIndexChanged(object sender, EventArgs e)
        {
            CalcularTotal();
        }

        private void CalcularTotal()
        {
            if (nudQuantidade.Value != 0 && lstLote.SelectedItem != null)
            {
                compra.Quantidade = Convert.ToInt16(nudQuantidade.Value);
                compra.Produto = (Produto)lstLote.SelectedItem;
                lblTotal.Text = "Total: R$ " + compra.calcularTotal();
            }
        }


        private void txtLote_TextChanged(object sender, EventArgs e)
        {
            
        }
    }
}
