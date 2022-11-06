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
        public NovoLote()
        {
            InitializeComponent();
        }
        public static Compras compra;
        static NovoLote()
        {
            compra = new Compras();
        }
        public static NovoLote instance { get; set;  }

        public static NovoLote GetInstance()
        {
            if (instance == null
                || instance.IsDisposed)
            {
                instance = new NovoLote();
            }
            return instance;
        }

        private void txtLote_TextChanged(object sender, EventArgs e)
        {

        }

        private void dtpCompra_ValueChanged(object sender, EventArgs e)
        {

        }

        private void dtpVencimento_ValueChanged(object sender, EventArgs e)
        {

        }

        private void txtProduto_TextChanged(object sender, EventArgs e)
        {
            listBox1.DataSource = BancoDeDados.Busca(txtProduto.Text);
        }

        private void nupQuantidade_ValueChanged(object sender, EventArgs e)
        {
            CalcularTotal();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            CalcularTotal();
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
                compra.Compra = dtpCompra.Value;
                compra.Vencimento = dtpVencimento.Value;
            }
            catch
            {
                MessageBox.Show("data", "Erro");
                return;
            }

            try
            {
                compra.Quantidade = Convert.ToInt16(nupQuantidade.Value);
            }
            catch
            {
                MessageBox.Show("quantidade", "Erro");
                return;
            }

            if (listBox1.SelectedItem == null)
            {
                MessageBox.Show("nenhum produto", "Erro");
                return;
            }
            else
            {
                compra.Produto = (Produto)listBox1.SelectedItem;
            }

            BancoDeDados.Compras.Add(compra);
            compra = new Compras();

            txtProduto.Text = "";
            txtLote.Text = "";
            dtpCompra.Value = DateTime.Now;
            dtpVencimento.Value = DateTime.Now.AddDays(1);
            nupQuantidade.Value = 1;
            lblTotal.Text = "Total R$ ";
            listBox1.DataSource = null;
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            this.Close();
        }
        private void CalcularTotal()
        {
            if (nupQuantidade.Value != 0 && listBox1.SelectedItem != null)
            {
                compra.Quantidade = Convert.ToInt16(nupQuantidade.Value);
                compra.Produto = (Produto)listBox1.SelectedItem;
                lblTotal.Text = "Total R$ " + compra.CalcularTotal();
            }
        }
    }
}
