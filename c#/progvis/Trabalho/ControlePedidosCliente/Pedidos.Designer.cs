namespace ControlePedidosCliente
{
    partial class Pedidos
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
            this.tlbPedidos = new System.Windows.Forms.TableLayoutPanel();
            this.lbPedidos = new System.Windows.Forms.ListBox();
            this.btnNew = new System.Windows.Forms.Button();
            this.tlbPedidos.SuspendLayout();
            this.SuspendLayout();
            // 
            // tlbPedidos
            // 
            this.tlbPedidos.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tlbPedidos.ColumnCount = 1;
            this.tlbPedidos.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlbPedidos.Controls.Add(this.lbPedidos, 0, 0);
            this.tlbPedidos.Controls.Add(this.btnNew, 0, 1);
            this.tlbPedidos.Location = new System.Drawing.Point(12, 12);
            this.tlbPedidos.Name = "tlbPedidos";
            this.tlbPedidos.RowCount = 2;
            this.tlbPedidos.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tlbPedidos.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 62F));
            this.tlbPedidos.Size = new System.Drawing.Size(269, 426);
            this.tlbPedidos.TabIndex = 0;
            // 
            // lbPedidos
            // 
            this.lbPedidos.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.lbPedidos.FormattingEnabled = true;
            this.lbPedidos.Location = new System.Drawing.Point(3, 3);
            this.lbPedidos.Name = "lbPedidos";
            this.lbPedidos.Size = new System.Drawing.Size(263, 355);
            this.lbPedidos.TabIndex = 0;
            // 
            // btnNew
            // 
            this.btnNew.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.btnNew.Location = new System.Drawing.Point(3, 367);
            this.btnNew.Name = "btnNew";
            this.btnNew.Size = new System.Drawing.Size(263, 56);
            this.btnNew.TabIndex = 1;
            this.btnNew.Text = "Novo Pedido";
            this.btnNew.UseVisualStyleBackColor = true;
            this.btnNew.Click += new System.EventHandler(this.btnNew_Click);
            // 
            // Pedidos
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(293, 450);
            this.Controls.Add(this.tlbPedidos);
            this.Name = "Pedidos";
            this.Text = "Pedidos";
            this.tlbPedidos.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TableLayoutPanel tlbPedidos;
        private System.Windows.Forms.ListBox lbPedidos;
        private System.Windows.Forms.Button btnNew;
    }
}