namespace ControleDeNotas
{
    partial class NovaNota
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(NovaNota));
            this.tlpPrincipal = new System.Windows.Forms.TableLayoutPanel();
            this.lstProdutos = new System.Windows.Forms.ListBox();
            this.tlpBotoes = new System.Windows.Forms.TableLayoutPanel();
            this.btnSalvar = new System.Windows.Forms.Button();
            this.btnCancelar = new System.Windows.Forms.Button();
            this.tlpQuantidade = new System.Windows.Forms.TableLayoutPanel();
            this.label1 = new System.Windows.Forms.Label();
            this.nudQuantidade = new System.Windows.Forms.NumericUpDown();
            this.tlpVencimento = new System.Windows.Forms.TableLayoutPanel();
            this.dtpVencimento = new System.Windows.Forms.DateTimePicker();
            this.lblV = new System.Windows.Forms.Label();
            this.tlpProduto = new System.Windows.Forms.TableLayoutPanel();
            this.txtProduto = new System.Windows.Forms.TextBox();
            this.lblProduto = new System.Windows.Forms.Label();
            this.tlpCadastro = new System.Windows.Forms.TableLayoutPanel();
            this.lblC = new System.Windows.Forms.Label();
            this.dtpCadastro = new System.Windows.Forms.DateTimePicker();
            this.tlpLote = new System.Windows.Forms.TableLayoutPanel();
            this.lblLote = new System.Windows.Forms.Label();
            this.txtLote = new System.Windows.Forms.TextBox();
            this.tlpTotal = new System.Windows.Forms.TableLayoutPanel();
            this.lblTotal = new System.Windows.Forms.Label();
            this.notifyIcon1 = new System.Windows.Forms.NotifyIcon(this.components);
            this.tlpPrincipal.SuspendLayout();
            this.tlpBotoes.SuspendLayout();
            this.tlpQuantidade.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nudQuantidade)).BeginInit();
            this.tlpVencimento.SuspendLayout();
            this.tlpProduto.SuspendLayout();
            this.tlpCadastro.SuspendLayout();
            this.tlpLote.SuspendLayout();
            this.tlpTotal.SuspendLayout();
            this.SuspendLayout();
            // 
            // tlpPrincipal
            // 
            this.tlpPrincipal.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tlpPrincipal.ColumnCount = 2;
            this.tlpPrincipal.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpPrincipal.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpPrincipal.Controls.Add(this.lstProdutos, 0, 2);
            this.tlpPrincipal.Controls.Add(this.tlpBotoes, 1, 3);
            this.tlpPrincipal.Controls.Add(this.tlpQuantidade, 0, 3);
            this.tlpPrincipal.Controls.Add(this.tlpVencimento, 1, 1);
            this.tlpPrincipal.Controls.Add(this.tlpProduto, 0, 1);
            this.tlpPrincipal.Controls.Add(this.tlpCadastro, 1, 0);
            this.tlpPrincipal.Controls.Add(this.tlpLote, 0, 0);
            this.tlpPrincipal.Controls.Add(this.tlpTotal, 1, 2);
            this.tlpPrincipal.Location = new System.Drawing.Point(21, 25);
            this.tlpPrincipal.Margin = new System.Windows.Forms.Padding(0);
            this.tlpPrincipal.Name = "tlpPrincipal";
            this.tlpPrincipal.RowCount = 4;
            this.tlpPrincipal.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 10F));
            this.tlpPrincipal.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 10F));
            this.tlpPrincipal.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 70F));
            this.tlpPrincipal.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 10F));
            this.tlpPrincipal.Size = new System.Drawing.Size(544, 366);
            this.tlpPrincipal.TabIndex = 0;
            // 
            // lstProdutos
            // 
            this.lstProdutos.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lstProdutos.FormattingEnabled = true;
            this.lstProdutos.Location = new System.Drawing.Point(3, 75);
            this.lstProdutos.Name = "lstProdutos";
            this.lstProdutos.Size = new System.Drawing.Size(266, 238);
            this.lstProdutos.TabIndex = 0;
            this.lstProdutos.SelectedIndexChanged += new System.EventHandler(this.lstProdutos_SelectedIndexChanged);
            // 
            // tlpBotoes
            // 
            this.tlpBotoes.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tlpBotoes.ColumnCount = 2;
            this.tlpBotoes.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpBotoes.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 136F));
            this.tlpBotoes.Controls.Add(this.btnSalvar, 1, 0);
            this.tlpBotoes.Controls.Add(this.btnCancelar, 0, 0);
            this.tlpBotoes.Location = new System.Drawing.Point(272, 328);
            this.tlpBotoes.Margin = new System.Windows.Forms.Padding(0);
            this.tlpBotoes.Name = "tlpBotoes";
            this.tlpBotoes.RowCount = 1;
            this.tlpBotoes.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpBotoes.Size = new System.Drawing.Size(272, 38);
            this.tlpBotoes.TabIndex = 4;
            // 
            // btnSalvar
            // 
            this.btnSalvar.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.btnSalvar.Location = new System.Drawing.Point(139, 3);
            this.btnSalvar.Name = "btnSalvar";
            this.btnSalvar.Size = new System.Drawing.Size(130, 32);
            this.btnSalvar.TabIndex = 4;
            this.btnSalvar.Text = "SALVAR";
            this.btnSalvar.UseVisualStyleBackColor = true;
            this.btnSalvar.Click += new System.EventHandler(this.btnSalvar_Click);
            // 
            // btnCancelar
            // 
            this.btnCancelar.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.btnCancelar.Location = new System.Drawing.Point(3, 3);
            this.btnCancelar.Name = "btnCancelar";
            this.btnCancelar.Size = new System.Drawing.Size(130, 32);
            this.btnCancelar.TabIndex = 5;
            this.btnCancelar.Text = "CANCELAR";
            this.btnCancelar.UseVisualStyleBackColor = true;
            this.btnCancelar.Click += new System.EventHandler(this.btnCancelar_Click);
            // 
            // tlpQuantidade
            // 
            this.tlpQuantidade.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tlpQuantidade.ColumnCount = 2;
            this.tlpQuantidade.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpQuantidade.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 181F));
            this.tlpQuantidade.Controls.Add(this.label1, 0, 0);
            this.tlpQuantidade.Controls.Add(this.nudQuantidade, 1, 0);
            this.tlpQuantidade.Location = new System.Drawing.Point(0, 328);
            this.tlpQuantidade.Margin = new System.Windows.Forms.Padding(0);
            this.tlpQuantidade.Name = "tlpQuantidade";
            this.tlpQuantidade.RowCount = 1;
            this.tlpQuantidade.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpQuantidade.Size = new System.Drawing.Size(272, 38);
            this.tlpQuantidade.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(3, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(85, 38);
            this.label1.TabIndex = 2;
            this.label1.Text = "QUANTIDADE:";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // nudQuantidade
            // 
            this.nudQuantidade.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.nudQuantidade.Location = new System.Drawing.Point(94, 9);
            this.nudQuantidade.Maximum = new decimal(new int[] {
            32767,
            0,
            0,
            0});
            this.nudQuantidade.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.nudQuantidade.Name = "nudQuantidade";
            this.nudQuantidade.Size = new System.Drawing.Size(175, 20);
            this.nudQuantidade.TabIndex = 2;
            this.nudQuantidade.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.nudQuantidade.ValueChanged += new System.EventHandler(this.nudQuantidade_ValueChanged);
            // 
            // tlpVencimento
            // 
            this.tlpVencimento.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tlpVencimento.ColumnCount = 2;
            this.tlpVencimento.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpVencimento.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 152F));
            this.tlpVencimento.Controls.Add(this.dtpVencimento, 1, 0);
            this.tlpVencimento.Controls.Add(this.lblV, 0, 0);
            this.tlpVencimento.Location = new System.Drawing.Point(272, 36);
            this.tlpVencimento.Margin = new System.Windows.Forms.Padding(0);
            this.tlpVencimento.Name = "tlpVencimento";
            this.tlpVencimento.RowCount = 1;
            this.tlpVencimento.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpVencimento.Size = new System.Drawing.Size(272, 36);
            this.tlpVencimento.TabIndex = 3;
            // 
            // dtpVencimento
            // 
            this.dtpVencimento.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.dtpVencimento.Format = System.Windows.Forms.DateTimePickerFormat.Short;
            this.dtpVencimento.Location = new System.Drawing.Point(123, 8);
            this.dtpVencimento.Name = "dtpVencimento";
            this.dtpVencimento.Size = new System.Drawing.Size(146, 20);
            this.dtpVencimento.TabIndex = 3;
            // 
            // lblV
            // 
            this.lblV.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lblV.AutoSize = true;
            this.lblV.Location = new System.Drawing.Point(3, 0);
            this.lblV.Name = "lblV";
            this.lblV.Size = new System.Drawing.Size(114, 36);
            this.lblV.TabIndex = 3;
            this.lblV.Text = "DATA VENCIMENTO";
            this.lblV.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // tlpProduto
            // 
            this.tlpProduto.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tlpProduto.ColumnCount = 2;
            this.tlpProduto.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpProduto.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 195F));
            this.tlpProduto.Controls.Add(this.txtProduto, 1, 0);
            this.tlpProduto.Controls.Add(this.lblProduto, 0, 0);
            this.tlpProduto.Location = new System.Drawing.Point(0, 36);
            this.tlpProduto.Margin = new System.Windows.Forms.Padding(0);
            this.tlpProduto.Name = "tlpProduto";
            this.tlpProduto.RowCount = 1;
            this.tlpProduto.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpProduto.Size = new System.Drawing.Size(272, 36);
            this.tlpProduto.TabIndex = 1;
            // 
            // txtProduto
            // 
            this.txtProduto.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.txtProduto.Location = new System.Drawing.Point(80, 8);
            this.txtProduto.MaxLength = 2147483647;
            this.txtProduto.Name = "txtProduto";
            this.txtProduto.Size = new System.Drawing.Size(189, 20);
            this.txtProduto.TabIndex = 1;
            this.txtProduto.TextChanged += new System.EventHandler(this.txtProduto_TextChanged);
            // 
            // lblProduto
            // 
            this.lblProduto.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lblProduto.AutoSize = true;
            this.lblProduto.Location = new System.Drawing.Point(3, 0);
            this.lblProduto.Name = "lblProduto";
            this.lblProduto.Size = new System.Drawing.Size(71, 36);
            this.lblProduto.TabIndex = 0;
            this.lblProduto.Text = "PRODUTO:";
            this.lblProduto.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // tlpCadastro
            // 
            this.tlpCadastro.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tlpCadastro.ColumnCount = 2;
            this.tlpCadastro.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpCadastro.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 152F));
            this.tlpCadastro.Controls.Add(this.lblC, 0, 0);
            this.tlpCadastro.Controls.Add(this.dtpCadastro, 1, 0);
            this.tlpCadastro.Location = new System.Drawing.Point(272, 0);
            this.tlpCadastro.Margin = new System.Windows.Forms.Padding(0);
            this.tlpCadastro.Name = "tlpCadastro";
            this.tlpCadastro.RowCount = 1;
            this.tlpCadastro.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpCadastro.Size = new System.Drawing.Size(272, 36);
            this.tlpCadastro.TabIndex = 10;
            // 
            // lblC
            // 
            this.lblC.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lblC.AutoSize = true;
            this.lblC.Location = new System.Drawing.Point(3, 0);
            this.lblC.Name = "lblC";
            this.lblC.Size = new System.Drawing.Size(114, 36);
            this.lblC.TabIndex = 10;
            this.lblC.Text = "DATA CADASTRO:";
            this.lblC.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // dtpCadastro
            // 
            this.dtpCadastro.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.dtpCadastro.Format = System.Windows.Forms.DateTimePickerFormat.Short;
            this.dtpCadastro.Location = new System.Drawing.Point(123, 8);
            this.dtpCadastro.Name = "dtpCadastro";
            this.dtpCadastro.Size = new System.Drawing.Size(146, 20);
            this.dtpCadastro.TabIndex = 10;
            // 
            // tlpLote
            // 
            this.tlpLote.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tlpLote.ColumnCount = 2;
            this.tlpLote.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpLote.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 196F));
            this.tlpLote.Controls.Add(this.lblLote, 0, 0);
            this.tlpLote.Controls.Add(this.txtLote, 1, 0);
            this.tlpLote.Location = new System.Drawing.Point(0, 0);
            this.tlpLote.Margin = new System.Windows.Forms.Padding(0);
            this.tlpLote.Name = "tlpLote";
            this.tlpLote.RowCount = 1;
            this.tlpLote.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpLote.Size = new System.Drawing.Size(272, 36);
            this.tlpLote.TabIndex = 0;
            // 
            // lblLote
            // 
            this.lblLote.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lblLote.AutoSize = true;
            this.lblLote.Location = new System.Drawing.Point(3, 0);
            this.lblLote.Name = "lblLote";
            this.lblLote.Size = new System.Drawing.Size(70, 36);
            this.lblLote.TabIndex = 0;
            this.lblLote.Text = "LOTE:";
            this.lblLote.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // txtLote
            // 
            this.txtLote.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right)));
            this.txtLote.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.txtLote.Location = new System.Drawing.Point(79, 8);
            this.txtLote.MaxLength = 2147483647;
            this.txtLote.Name = "txtLote";
            this.txtLote.Size = new System.Drawing.Size(190, 20);
            this.txtLote.TabIndex = 0;
            this.txtLote.TextChanged += new System.EventHandler(this.txtLote_TextChanged);
            // 
            // tlpTotal
            // 
            this.tlpTotal.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tlpTotal.ColumnCount = 1;
            this.tlpTotal.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpTotal.Controls.Add(this.lblTotal, 0, 0);
            this.tlpTotal.Location = new System.Drawing.Point(272, 72);
            this.tlpTotal.Margin = new System.Windows.Forms.Padding(0);
            this.tlpTotal.Name = "tlpTotal";
            this.tlpTotal.RowCount = 1;
            this.tlpTotal.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlpTotal.Size = new System.Drawing.Size(272, 256);
            this.tlpTotal.TabIndex = 8;
            // 
            // lblTotal
            // 
            this.lblTotal.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.lblTotal.AutoSize = true;
            this.lblTotal.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTotal.ForeColor = System.Drawing.Color.Red;
            this.lblTotal.Location = new System.Drawing.Point(56, 227);
            this.lblTotal.Name = "lblTotal";
            this.lblTotal.Size = new System.Drawing.Size(213, 29);
            this.lblTotal.TabIndex = 99;
            this.lblTotal.Text = "TOTAL: R$ 00.00";
            // 
            // notifyIcon1
            // 
            this.notifyIcon1.BalloonTipIcon = System.Windows.Forms.ToolTipIcon.Info;
            this.notifyIcon1.BalloonTipText = "Não se esqueça de atualizar as tabelas abertas !";
            this.notifyIcon1.BalloonTipTitle = "Alerta";
            this.notifyIcon1.Icon = ((System.Drawing.Icon)(resources.GetObject("notifyIcon1.Icon")));
            this.notifyIcon1.Text = "notifyIcon1";
            this.notifyIcon1.Visible = true;
            // 
            // NovaNota
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(577, 403);
            this.Controls.Add(this.tlpPrincipal);
            this.MaximizeBox = false;
            this.Name = "NovaNota";
            this.Text = "NovaNota";
            this.tlpPrincipal.ResumeLayout(false);
            this.tlpBotoes.ResumeLayout(false);
            this.tlpQuantidade.ResumeLayout(false);
            this.tlpQuantidade.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nudQuantidade)).EndInit();
            this.tlpVencimento.ResumeLayout(false);
            this.tlpVencimento.PerformLayout();
            this.tlpProduto.ResumeLayout(false);
            this.tlpProduto.PerformLayout();
            this.tlpCadastro.ResumeLayout(false);
            this.tlpCadastro.PerformLayout();
            this.tlpLote.ResumeLayout(false);
            this.tlpLote.PerformLayout();
            this.tlpTotal.ResumeLayout(false);
            this.tlpTotal.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TableLayoutPanel tlpPrincipal;
        private System.Windows.Forms.ListBox lstProdutos;
        private System.Windows.Forms.TableLayoutPanel tlpBotoes;
        private System.Windows.Forms.Button btnSalvar;
        private System.Windows.Forms.Button btnCancelar;
        private System.Windows.Forms.TableLayoutPanel tlpQuantidade;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.NumericUpDown nudQuantidade;
        private System.Windows.Forms.TableLayoutPanel tlpVencimento;
        private System.Windows.Forms.DateTimePicker dtpVencimento;
        private System.Windows.Forms.Label lblV;
        private System.Windows.Forms.TableLayoutPanel tlpProduto;
        private System.Windows.Forms.TextBox txtProduto;
        private System.Windows.Forms.Label lblProduto;
        private System.Windows.Forms.TableLayoutPanel tlpCadastro;
        private System.Windows.Forms.Label lblC;
        private System.Windows.Forms.DateTimePicker dtpCadastro;
        private System.Windows.Forms.TableLayoutPanel tlpLote;
        private System.Windows.Forms.Label lblLote;
        private System.Windows.Forms.TextBox txtLote;
        private System.Windows.Forms.TableLayoutPanel tlpTotal;
        private System.Windows.Forms.Label lblTotal;
        private System.Windows.Forms.NotifyIcon notifyIcon1;
    }
}