namespace ControlePedidosCliente
{
    partial class Produtos
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
            this.lbBdProdutos = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // lbBdProdutos
            // 
            this.lbBdProdutos.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbBdProdutos.FormattingEnabled = true;
            this.lbBdProdutos.ItemHeight = 24;
            this.lbBdProdutos.Location = new System.Drawing.Point(13, 13);
            this.lbBdProdutos.Name = "lbBdProdutos";
            this.lbBdProdutos.Size = new System.Drawing.Size(259, 388);
            this.lbBdProdutos.TabIndex = 0;
            // 
            // Produtos
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 437);
            this.Controls.Add(this.lbBdProdutos);
            this.Name = "Produtos";
            this.Text = "Produtos";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListBox lbBdProdutos;
    }
}