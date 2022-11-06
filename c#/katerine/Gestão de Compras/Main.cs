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
    public partial class Main : Form
    {
        public Main()
        {
            InitializeComponent();
        }

        private void Main_Load(object sender, EventArgs e)
        {

        }

        private void mnuArquivoSobre_Click(object sender, EventArgs e)
        {
            Sobre P = Sobre.GetInstance();
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();
        }

        private void mnuArquivoSair_Click(object sender, EventArgs e)
        {

        }

        private void mnuCadastroNovoLote_Click(object sender, EventArgs e)
        {
            NovoLote P = NovoLote.GetInstance();
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();
        }

        private void mnuRelatoriosTL_Click(object sender, EventArgs e)
        {
            TodosLotes P = TodosLotes.GetInstance();
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();
        }

        private void mnuRelatoriosVence1_Click(object sender, EventArgs e)
        {
            Vencimento1 P = Vencimento1.GetInstance();
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();

        }

        private void mnuRelatoriosVence5_Click(object sender, EventArgs e)
        {
            Vencimento5 P = Vencimento5.GetInstance();
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();
        }

        private void mnuRelatoriosVenciPerso_Click(object sender, EventArgs e)
        {
            VencimentoPersonalizado P = VencimentoPersonalizado.GetInstance();
            if (P.MdiParent == null)
            {
                P.MdiParent = this;
                P.Show();
            }
            else
            {
                P.WindowState = FormWindowState.Normal;
            }
            P.Activate();
        }
    }
}
