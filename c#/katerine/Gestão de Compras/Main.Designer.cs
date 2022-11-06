namespace Gestão_de_Compras
{
    partial class Main
    {
        /// <summary>
        /// Variável de designer necessária.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpar os recursos que estão sendo usados.
        /// </summary>
        /// <param name="disposing">true se for necessário descartar os recursos gerenciados; caso contrário, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código gerado pelo Windows Form Designer

        /// <summary>
        /// Método necessário para suporte ao Designer - não modifique 
        /// o conteúdo deste método com o editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Main));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.mnuArquivo = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuArquivoSobre = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuArquivoSair = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuCadastro = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuCadastroNovoLote = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRelatorios = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRelatoriosTL = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRelatoriosVence1 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRelatoriosVence5 = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuRelatoriosVenciPerso = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuArquivo,
            this.mnuCadastro,
            this.mnuRelatorios});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(778, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // mnuArquivo
            // 
            this.mnuArquivo.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuArquivoSobre,
            this.mnuArquivoSair});
            this.mnuArquivo.Name = "mnuArquivo";
            this.mnuArquivo.Size = new System.Drawing.Size(61, 20);
            this.mnuArquivo.Text = "Arquivo";
            // 
            // mnuArquivoSobre
            // 
            this.mnuArquivoSobre.Name = "mnuArquivoSobre";
            this.mnuArquivoSobre.Size = new System.Drawing.Size(180, 22);
            this.mnuArquivoSobre.Text = "Sobre";
            this.mnuArquivoSobre.Click += new System.EventHandler(this.mnuArquivoSobre_Click);
            // 
            // mnuArquivoSair
            // 
            this.mnuArquivoSair.Name = "mnuArquivoSair";
            this.mnuArquivoSair.Size = new System.Drawing.Size(180, 22);
            this.mnuArquivoSair.Text = "Sair";
            this.mnuArquivoSair.Click += new System.EventHandler(this.mnuArquivoSair_Click);
            // 
            // mnuCadastro
            // 
            this.mnuCadastro.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuCadastroNovoLote});
            this.mnuCadastro.Name = "mnuCadastro";
            this.mnuCadastro.Size = new System.Drawing.Size(66, 20);
            this.mnuCadastro.Text = "Cadastro";
            // 
            // mnuCadastroNovoLote
            // 
            this.mnuCadastroNovoLote.Name = "mnuCadastroNovoLote";
            this.mnuCadastroNovoLote.Size = new System.Drawing.Size(180, 22);
            this.mnuCadastroNovoLote.Text = "Novo Lote";
            this.mnuCadastroNovoLote.Click += new System.EventHandler(this.mnuCadastroNovoLote_Click);
            // 
            // mnuRelatorios
            // 
            this.mnuRelatorios.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuRelatoriosTL,
            this.mnuRelatoriosVence1,
            this.mnuRelatoriosVence5,
            this.mnuRelatoriosVenciPerso});
            this.mnuRelatorios.Name = "mnuRelatorios";
            this.mnuRelatorios.Size = new System.Drawing.Size(71, 20);
            this.mnuRelatorios.Text = "Relatórios";
            // 
            // mnuRelatoriosTL
            // 
            this.mnuRelatoriosTL.Name = "mnuRelatoriosTL";
            this.mnuRelatoriosTL.Size = new System.Drawing.Size(213, 22);
            this.mnuRelatoriosTL.Text = "Todos Lotes";
            this.mnuRelatoriosTL.Click += new System.EventHandler(this.mnuRelatoriosTL_Click);
            // 
            // mnuRelatoriosVence1
            // 
            this.mnuRelatoriosVence1.Name = "mnuRelatoriosVence1";
            this.mnuRelatoriosVence1.Size = new System.Drawing.Size(213, 22);
            this.mnuRelatoriosVence1.Text = "A vencer em até 1 dia";
            this.mnuRelatoriosVence1.Click += new System.EventHandler(this.mnuRelatoriosVence1_Click);
            // 
            // mnuRelatoriosVence5
            // 
            this.mnuRelatoriosVence5.Name = "mnuRelatoriosVence5";
            this.mnuRelatoriosVence5.Size = new System.Drawing.Size(213, 22);
            this.mnuRelatoriosVence5.Text = "A vencer em até 5 dias";
            this.mnuRelatoriosVence5.Click += new System.EventHandler(this.mnuRelatoriosVence5_Click);
            // 
            // mnuRelatoriosVenciPerso
            // 
            this.mnuRelatoriosVenciPerso.Name = "mnuRelatoriosVenciPerso";
            this.mnuRelatoriosVenciPerso.Size = new System.Drawing.Size(213, 22);
            this.mnuRelatoriosVenciPerso.Text = "Vencimento personalizado";
            this.mnuRelatoriosVenciPerso.Click += new System.EventHandler(this.mnuRelatoriosVenciPerso_Click);
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::Gestão_de_Compras.Properties.Resources._2512798_flor_flores_esboco_vetor_removebg_preview;
            this.ClientSize = new System.Drawing.Size(778, 545);
            this.Controls.Add(this.menuStrip1);
            this.ForeColor = System.Drawing.SystemColors.ControlText;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.IsMdiContainer = true;
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Main";
            this.Text = "Supermercado BellaFlor";
            this.Load += new System.EventHandler(this.Main_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem mnuArquivo;
        private System.Windows.Forms.ToolStripMenuItem mnuArquivoSobre;
        private System.Windows.Forms.ToolStripMenuItem mnuArquivoSair;
        private System.Windows.Forms.ToolStripMenuItem mnuCadastro;
        private System.Windows.Forms.ToolStripMenuItem mnuCadastroNovoLote;
        private System.Windows.Forms.ToolStripMenuItem mnuRelatorios;
        private System.Windows.Forms.ToolStripMenuItem mnuRelatoriosTL;
        private System.Windows.Forms.ToolStripMenuItem mnuRelatoriosVence1;
        private System.Windows.Forms.ToolStripMenuItem mnuRelatoriosVence5;
        private System.Windows.Forms.ToolStripMenuItem mnuRelatoriosVenciPerso;
    }
}

