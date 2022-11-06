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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            IsMdiContainer = true;
        }

        private void mnuSobre_Click(object sender, EventArgs e)
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

        private void mnuSair_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void mnuLote_Click(object sender, EventArgs e)
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

        private void todosLotesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            TodosOsLotes P = TodosOsLotes.GetInstance();
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

        private void aVencerEmAté1DiaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            VencimentoUm P = VencimentoUm.GetInstance();
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

        private void vencimentoPersonalizadoToolStripMenuItem_Click(object sender, EventArgs e)
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

        private void aVencerEmAtéDiasToolStripMenuItem_Click(object sender, EventArgs e)
        {
            VencimentoCinco P = VencimentoCinco.GetInstance();
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
