namespace Gestão_de_Compras
{
    partial class Form1
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
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.mnuArquivo = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuSobre = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuSair = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuCadastro = new System.Windows.Forms.ToolStripMenuItem();
            this.mnuLote = new System.Windows.Forms.ToolStripMenuItem();
            this.relatóriosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.todosLotesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aVencerEmAté1DiaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aVencerEmAtéDiasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.vencimentoPersonalizadoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuArquivo,
            this.mnuCadastro,
            this.relatóriosToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(816, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // mnuArquivo
            // 
            this.mnuArquivo.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuSobre,
            this.mnuSair});
            this.mnuArquivo.Name = "mnuArquivo";
            this.mnuArquivo.Size = new System.Drawing.Size(64, 20);
            this.mnuArquivo.Text = "Arquivo ";
            // 
            // mnuSobre
            // 
            this.mnuSobre.Name = "mnuSobre";
            this.mnuSobre.Size = new System.Drawing.Size(104, 22);
            this.mnuSobre.Text = "Sobre";
            this.mnuSobre.Click += new System.EventHandler(this.mnuSobre_Click);
            // 
            // mnuSair
            // 
            this.mnuSair.Name = "mnuSair";
            this.mnuSair.Size = new System.Drawing.Size(104, 22);
            this.mnuSair.Text = "Sair";
            this.mnuSair.Click += new System.EventHandler(this.mnuSair_Click);
            // 
            // mnuCadastro
            // 
            this.mnuCadastro.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mnuLote});
            this.mnuCadastro.Name = "mnuCadastro";
            this.mnuCadastro.Size = new System.Drawing.Size(66, 20);
            this.mnuCadastro.Text = "Cadastro";
            // 
            // mnuLote
            // 
            this.mnuLote.Name = "mnuLote";
            this.mnuLote.Size = new System.Drawing.Size(129, 22);
            this.mnuLote.Text = "Novo Lote";
            this.mnuLote.Click += new System.EventHandler(this.mnuLote_Click);
            // 
            // relatóriosToolStripMenuItem
            // 
            this.relatóriosToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.todosLotesToolStripMenuItem,
            this.aVencerEmAté1DiaToolStripMenuItem,
            this.aVencerEmAtéDiasToolStripMenuItem,
            this.vencimentoPersonalizadoToolStripMenuItem});
            this.relatóriosToolStripMenuItem.Name = "relatóriosToolStripMenuItem";
            this.relatóriosToolStripMenuItem.Size = new System.Drawing.Size(71, 20);
            this.relatóriosToolStripMenuItem.Text = "Relatórios";
            // 
            // todosLotesToolStripMenuItem
            // 
            this.todosLotesToolStripMenuItem.Name = "todosLotesToolStripMenuItem";
            this.todosLotesToolStripMenuItem.Size = new System.Drawing.Size(216, 22);
            this.todosLotesToolStripMenuItem.Text = "Todos Lotes";
            this.todosLotesToolStripMenuItem.Click += new System.EventHandler(this.todosLotesToolStripMenuItem_Click);
            // 
            // aVencerEmAté1DiaToolStripMenuItem
            // 
            this.aVencerEmAté1DiaToolStripMenuItem.Name = "aVencerEmAté1DiaToolStripMenuItem";
            this.aVencerEmAté1DiaToolStripMenuItem.Size = new System.Drawing.Size(216, 22);
            this.aVencerEmAté1DiaToolStripMenuItem.Text = "A vencer em até 1 dia";
            this.aVencerEmAté1DiaToolStripMenuItem.Click += new System.EventHandler(this.aVencerEmAté1DiaToolStripMenuItem_Click);
            // 
            // aVencerEmAtéDiasToolStripMenuItem
            // 
            this.aVencerEmAtéDiasToolStripMenuItem.Name = "aVencerEmAtéDiasToolStripMenuItem";
            this.aVencerEmAtéDiasToolStripMenuItem.Size = new System.Drawing.Size(216, 22);
            this.aVencerEmAtéDiasToolStripMenuItem.Text = "A vencer em até  5 dias ";
            this.aVencerEmAtéDiasToolStripMenuItem.Click += new System.EventHandler(this.aVencerEmAtéDiasToolStripMenuItem_Click);
            // 
            // vencimentoPersonalizadoToolStripMenuItem
            // 
            this.vencimentoPersonalizadoToolStripMenuItem.Name = "vencimentoPersonalizadoToolStripMenuItem";
            this.vencimentoPersonalizadoToolStripMenuItem.Size = new System.Drawing.Size(216, 22);
            this.vencimentoPersonalizadoToolStripMenuItem.Text = "Vencimento Personalizado ";
            this.vencimentoPersonalizadoToolStripMenuItem.Click += new System.EventHandler(this.vencimentoPersonalizadoToolStripMenuItem_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(816, 514);
            this.Controls.Add(this.menuStrip1);
            this.IsMdiContainer = true;
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "Supermercado";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem mnuArquivo;
        private System.Windows.Forms.ToolStripMenuItem mnuSobre;
        private System.Windows.Forms.ToolStripMenuItem mnuSair;
        private System.Windows.Forms.ToolStripMenuItem mnuCadastro;
        private System.Windows.Forms.ToolStripMenuItem mnuLote;
        private System.Windows.Forms.ToolStripMenuItem relatóriosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem todosLotesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aVencerEmAté1DiaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aVencerEmAtéDiasToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem vencimentoPersonalizadoToolStripMenuItem;
    }
}

