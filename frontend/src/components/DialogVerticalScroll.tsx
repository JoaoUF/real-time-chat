import DialogTitle from "@mui/joy/DialogTitle";
import List from "@mui/joy/List";
import ListItem from "@mui/joy/ListItem";
import Modal from "@mui/joy/Modal";
import ModalClose from "@mui/joy/ModalClose";
import ModalDialog from "@mui/joy/ModalDialog";

type DialogVerticalScrollProps = {
  layout: any;
  setLayout: any;
};

export default function DialogVerticalScroll(props: DialogVerticalScrollProps) {
  const { layout, setLayout } = props;
  return (
    <Modal
      open={!!layout}
      onClose={() => {
        setLayout(undefined);
      }}
    >
      <ModalDialog layout={layout}>
        <ModalClose />
        <DialogTitle>Chat with</DialogTitle>
        <List
          sx={[
            {
              mx: "calc(-1 * var(--ModalDialog-padding))",
              px: "var(--ModalDialog-padding)",
            },
            { overflow: "scroll" },
          ]}
        >
          {[...Array(100)].map((item, index) => (
            <ListItem key={index}>I&apos;m in a scrollable area.</ListItem>
          ))}
        </List>
      </ModalDialog>
    </Modal>
  );
}
