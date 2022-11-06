using Gestão_de_Compras;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ControleDeNotas
{
    public partial class NovaNota : Form
    {
        private NovaNota()
        {
            InitializeComponent();
            dtpVencimento.Value = DateTime.Now.AddDays(1).Date;
        }
        public static Compra compra;
        static NovaNota()
        {
            compra = new Compra();
        }
        private static NovaNota instance { get; set; }
        public static NovaNota GetInstance()
        {

            if (instance == null || instance.IsDisposed)
            {
                instance = new NovaNota();
            }
            return instance;
        }

        private void txtLote_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtProduto_TextChanged(object sender, EventArgs e)
        {
            if (txtProduto.Text == "")
            {
                return;
            }
            lstProdutos.DataSource = BancoDeDados.Buscar(txtProduto.Text);
            CalcularTotal();
        }

        private void nudQuantidade_ValueChanged(object sender, EventArgs e)
        {
            CalcularTotal();
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            compra = null;
            this.Close();
        }

        private void btnSalvar_Click(object sender, EventArgs e)
        {
            try
            {
                Compra lote = BancoDeDados.VerificarLote(Convert.ToInt64(txtLote.Text)); //Verifica se existe um lote com o codigo e retorna ele
                if (lote != null)
                {
                    DialogResult pergunta = MessageBox.Show("Este Lote já existe, deseja atualizar o existente?", "ALERTA", MessageBoxButtons.OKCancel);
                    if (pergunta == DialogResult.OK)
                    {
                        compra = lote;
                        if(AdicionarItem())
                        {
                            LimparTela();
                            return;
                        }

                    }
                    else if (pergunta == DialogResult.Cancel)
                    {
                        txtLote.Text = "";
                        return;
                    }
                }
            }
            catch
            {
            }
            if (AdicionarItem()) // Verifica se nenhum erro foi encontrado
            {
                AdicionarNoBancoDeDados();
                LimparTela();
            }

        }

        private void lstProdutos_SelectedIndexChanged(object sender, EventArgs e)
        {
            CalcularTotal();
        }
        private void CalcularTotal()
        {
            if (nudQuantidade.Value != 0 && lstProdutos.SelectedItem != null)
            {
                compra.Quantidade = Convert.ToInt16(nudQuantidade.Value);
                compra.Produto = (Produto)lstProdutos.SelectedItem;
                lblTotal.Text = "TOTAL: R$ " + compra.CalcularTotal();
            }

        }
        private void LimparTela()
        {
            BancoDeDados.Compras.ResetBindings(); // Atualiza a lista novamente, pois bindingList não atualiza quando muda um valor

            txtProduto.Text = "";
            txtLote.Text = "";
            dtpCadastro.Value = DateTime.Now.Date;
            dtpVencimento.Value = DateTime.Now.AddDays(1).Date;
            nudQuantidade.Value = 1;
            lblTotal.Text = "TOTAL: R$ 00.00";
            lstProdutos.DataSource = null;

            compra = new Compra();
        }

        private bool AdicionarItem()
        {
            try
            {
                compra.Lote = Convert.ToInt64(txtLote.Text);
            }
            catch
            {
                MessageBox.Show("Lote inválido", "Erro");
                return false;
            }
            try
            {
                compra.DataCompra = dtpCadastro.Value.Date;
                compra.Vencimento = dtpVencimento.Value.Date;
            }
            catch
            {
                MessageBox.Show("Datas inválidas", "Erro");
                return false;
            }
            try
            {
                compra.Quantidade = Convert.ToInt16(nudQuantidade.Value);
            }
            catch
            {
                MessageBox.Show("Quantidade Inválida", "Erro");
                return false;
            }
            if (lstProdutos.SelectedItem == null)
            {
                MessageBox.Show("Produto inválido", "Erro");
                return false;
            }
            else
            {
                compra.Produto = (Produto)lstProdutos.SelectedItem;
            }
            return true;

        }

        private void AdicionarNoBancoDeDados()
        {
            BancoDeDados.Compras.Add(compra);

            notifyIcon1.ShowBalloonTip(1000);

            compra = new Compra();
        }

        private void AtualizarJanelas()
        {
            try
            {
                Vencimentos.GetInstance(1).F5();
            }
            catch { }
            try
            {
                Vencimentos.GetInstance(1).F5();
            }
            catch { }

        }
    }
}
